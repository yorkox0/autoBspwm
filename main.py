import os, time

def menu():
    print("1 -> Instalar Requerimientos necesarios")
    print("\n2 -> Instalar bspwm")
    print("\n3 -> Instalar Polybar")
    print("\n4 -> Salir")

    option = input("\n-->> ")

    if option == "1":
        requeriments()
    if option == "2":
        bspwm()
    if option == "3":
        polybar()
    if option == "4":
        exit()

def requerimets():
    print("[+] Instalando requerimientos...\n")

    # Instalando Requerimientos
    os.system("sudo apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y")
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y")
    os.system("sudo apt install bspwm rofi caja feh firefox")

    time.sleep(2)
    print("[+] Requetimientos instalados correctamente")
    while True:
        menu()

def bspwm():
    # Instalando bspwm
    os.system("git clone https://github.com/baskerville/bspwm.git")
    os.system("mv bspwm/* .")
    os.system("rm -r bspwm/")
    os.system("make")
    os.system("sudo make install")
    os.system("rm -r artworks/ contrib/ doc/ src/ tests/ bspc bspc.o bspwm bspwm.o desktop.o events.o ewmh.o geometry.o helpers.o history.o jsmn.o LICENSE Makefile messages.o monitor.o parse.o pointer.o query.o README.md restore.o rule.o settings.o Sourcedeps stack.o subscribe.o tree.o VERSION window.o")
    os.system("git clone https://github.com/baskerville/sxhkd.git")
    os.system("mv sxhkd/* .")
    os.system("rm -r sxhkd/")
    os.system("cd ../sxhkd")
    os.system("make")
    os.system("sudo make install")
    os.system("mkdir ~/.config/bspwm")
    os.system("mkdir ~/.config/sxhkd")
    os.system("cp examples/bspwmrc ~/.config/bspwm/")
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.system("cp examples/sxhkdrc ~/.config/sxhkd/")
    os.system("rm -r contrib/ doc/ examples/ src/ grab.o helpers.o LICENSE Makefile parse.o README.md Sourcedeps sxhkd sxhkd.o types.o VERSION")
    print("\n[+] Bspwm instalado correctamente!")

if __name__ == '__main__':
    menu()
