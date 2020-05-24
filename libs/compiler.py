#!/usr/bin/python3
import sys
from os import chdir,system,getcwd,path,listdir,popen
from time import sleep
import code_translator

chdir(path.dirname(sys.argv[0]))
def create_sketch():
    print("[+] Create New Sketch ...\n")
    status = system("arduino-cli sketch new /tmp/{}".format(sketch))
    if status != 0:
        sleep(4)
        sys.exit(1)
def compile_sketch():
    print("[+] Compile Sketch ...\n")
    status = system("arduino-cli compile --fqbn {} /tmp/{}".format(fqbn,sketch))
    if status != 0:
        sleep(4)
        sys.exit()
def upload_sketch():
    print("[+] Upload Sketch ...\n")
    status = system("arduino-cli upload -p {} --fqbn {} /tmp/{}".format(PORT,fqbn,sketch))
    if status != 0:
        sleep(4)
        sys.exit()

def custom_command_attack(file):
    file = path.expanduser(file)
    print(getcwd())
    f = open("{}".format(script))
    sc = f.read()
    f.close()
    f = open(file)
    command = f.read()
    f.close()
    command = code_translator.code_translator(command)
    command = "\t"+command.output
    sc = sc.replace("<USER COMMAND>",command)
    f = open("/tmp/{}/{}.ino".format(sketch,sketch),"w")
    f.write(sc)
    f.close()



system("clear")
print("----------------")
PORT = sys.argv[1]
batchfile = sys.argv[2]
script = "RunaCustomCommandinCMD.ino"
change_firmware_require = True
fqbn = "arduino:avr:uno"
micro = "atmega16u2"
sketch = path.basename(script).replace(".ino","")

print()
create_sketch()
sleep(1)
custom_command_attack(batchfile)
sleep(1)
compile_sketch()
sleep(1)
upload_sketch()

status = system("./change_firmware.sh ./firmwares/Arduino-keyboard-0.3.hex {}".format(micro))

system("rm -r /tmp/{}".format(sketch))
print("---------------------")
print("Done !")
print("Enjoy With Your Hacking Board :)")
sleep(4)
sys.exit()
