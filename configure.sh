#!/bin/bash
# HOSSEIN  AHMADI
# https://MrPython.blog.ir
###########################


user=$(id -u)

if (( $user != 0 ))
then
	echo "Please Run With Sudo :)";
	exit 1;
fi


chmod +x ./libs/change_firmware.sh
echo "Installing ...";
apt update;
apt install dfu-programmer -y
apt install python3-pip -y 
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=/usr/bin sh
arduino-cli config init
arduino-cli core update-index
arduino-cli board listall uno
arduino-cli core install arduino:avr

echo "Ok ! your Uno2Rubber Is Ready ... Enjoy :)";
