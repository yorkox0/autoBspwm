/*
	Author: s4vitar - https://youtube.com/watch?v=7L1WNU7fBec
*/

package main

import (
	"fmt"
	"flag"
	"context" // Done() struct{} || <- ctx.Done()
	"strings"
	"strconv"
	"log"
	"sync"
	"time"
	"net"
)

var (
	host = flag.String("host", "127.0.0.1", "Host o dirección IP a escanear")
	ports = flag.String("range", "1-65535", "Rango de puertos a comprobar: 80,443,1-65535,1000-2000, ...")
	threads = flag.Int("threads", 1000, "Número de hilos a usar")
	timeout = flag.Duration("timeout", 1*time.Second, "Segundos por puerto")
)

func processRange(ctx context.Context, r string) chan int {
	c := make(chan int) // c <- elemento
	done := ctx.Done()

	go func() {
		defer close(c)
		blocks := strings.Split(r, ",")

		for _, block := range blocks {
			rg := strings.Split(block, "-")
			var minPort, maxPort int
			var err error

			minPort, err = strconv.Atoi(rg[0])

			if err != nil {
				log.Print("No ha sido posible interpretar el rango: ", block)
				continue
			}

			if len(rg) == 1 {
				maxPort = minPort
			} else {
				maxPort, err = strconv.Atoi(rg[1])
				if err != nil {
					log.Print("No ha sido posible interpretar el rango: ", block)
					continue
				}
			}
			for port := minPort; port <= maxPort; port++ {
				select {
				case c <- port:
				case <-done:
					return
				}
			}
		}
	}()
	return c
}

func scanPorts(ctx context.Context, in <-chan int) chan string {
	out := make(chan string)
	done := ctx.Done()
	var wg sync.WaitGroup
	wg.Add(*threads)

	for i := 0; i < *threads; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for {
				select {
				case port, ok := <-in:
					if !ok {
						return
					}
					s := scanPort(port)
					select {
					case out <- s:
					case <-done:
						return
					}
				case <-done:
					return
				}
			}
		}()
	}
	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}

func scanPort(port int) string {
	addr := fmt.Sprintf("%s:%d", *host, port) // ip:puerto
	conn, err := net.DialTimeout("tcp", addr, *timeout)

	if err != nil {
		return fmt.Sprintf("%d: %s", port, err.Error())
	}

	conn.Close()

	return fmt.Sprintf("%d: Abierto", port)
}

func main() {
	ctx, cancel := context.WithCancel(context.Background()) // Definimos nuestro contexto
	defer cancel()

	flag.Parse()
	fmt.Printf("\n[*] Escaneando host %s (Puerto: %s)\n\n", *host, *ports)

	pR := processRange(ctx, *ports)
	sP := scanPorts(ctx, pR)

	for port := range sP {
		if strings.HasSuffix(port, ": Abierto") {
			fmt.Println(port)
		}
	}
}
