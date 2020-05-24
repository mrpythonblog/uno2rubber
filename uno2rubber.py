#!/usr/bin/python3
#####################################
# Project Name : Uno2Rubber         #
# Version : 1.0                     #
# Programmer : Hossein Ahmadi       #
# Weblog : MrPython.blog.ir         #
#####################################

from os import system,path,listdir
import sys
from time import sleep

menu_options = ["Make RubberDucky","Flash Standard Firmware"]
banner = """ _   _            ____  ____        _     _
| | | |_ __   ___|___ \|  _ \ _   _| |__ | |__   ___ _ __
| | | | '_ \ / _ \ __) | |_) | | | | '_ \| '_ \ / _ \ '__|
| |_| | | | | (_) / __/|  _ <| |_| | |_) | |_) |  __/ |
 \___/|_| |_|\___/_____|_| \_\\__,_|_.__/|_.__/ \___|_|
MrPython.blog.ir || Hossein Ahmadi
"""

class loop :
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            system("clear")
            print(banner)
            print()
            for i in range(len(menu_options)):
                print("[{}] {}".format(i+1,menu_options[i]))
            print("[99] EXIT")
            print()
            command = input(">> ")
            if command == "99":
                sys.exit()
            elif command == "1":
                self.makeboard()
                sys.exit()
            elif command == "2":
                if path.dirname(sys.argv[0]) != "":
                    system("{}libs/change_firmware.sh {} {}".format(path.dirname(sys.argv[0])+"/","{}/libs/firmwares/Arduino-usbserial-uno.hex".format(path.dirname(sys.argv[0])),"atmega16u2"))
                else:
                    system("libs/change_firmware.sh {} {}".format("./libs/firmwares/Arduino-usbserial-uno.hex","atmega16u2"))
                sys.exit()
    def makeboard(self):
        batchfile = input("BatchFile : ")
        if not path.isfile(batchfile):
            print("ERROR : There isn't {}".format(batchfile))
            sys.exit()
        PORT = input("PORT (Arduino PORT) : ")
        files = listdir("/dev")
        if not path.basename(PORT) in files:
            print("ERROR : {} Not Found !".format(PORT))
            sleep(4)
            sys.exit()
        del files
        if path.dirname(sys.argv[0]) != "":
            system("{}/libs/compiler.py {} {}".format(path.dirname(sys.argv[0]),PORT,path.abspath(batchfile)))
        else:
            system("python3 ./libs/compiler.py {} {}".format(PORT,batchfile))


if __name__ == "__main__":
    ap = loop()
