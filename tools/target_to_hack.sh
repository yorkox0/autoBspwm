#!/bin/bash
 
 # Mode of use: settarget <IP> <Name> or only settarget <Ip>
 
target=$(/usr/bin/cat ~/.config/bin/target | awk '{print $1}')
name=$(/usr/bin/cat ~/.config/bin/target | awk '{print $2}')

if [ $target ]; then
 
        status=$(/usr/bin/ping -c 1 $target | /usr/bin/grep "received" | /usr/bin/awk '{print $4}')
 
        if [ $status -ne 1 ]; then
                echo "%{F#FF0000} %{F#FFFFFF}$target $name%{u-}"
        else
            ttl=$(/usr/bin/ping -c 1 $target | /usr/bin/grep "ttl" | /usr/bin/awk '{print $6}' | /usr/bin/awk '{print $2}' FS==)
 
            if [ $ttl -le 64 ]; then
                echo "%{F#FF0000} %{F#FFFFFF}$target - $name%{u-}"
            elif [ $ttl -ge 65 -a $ttl -le 128 ]; then
                echo "%{F#FF0000} %{F#FFFFFF}$target - $name%{u-}"
            elif [ $ttl -ge 128 -a $ttl -le 254 ]; then
                echo "%{F#FF0000} %{F#FFFFFF}$target - $name%{u-}"
            else
                echo "%{F#FF0000}? %{F#FFFFFF}$target - $name%{u-}"
            fi
        fi
else
    echo "%{F#e51d0b}%{u-}%{F#ffffff} No target"
fi
