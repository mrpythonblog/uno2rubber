#!/bin/bash
# HOSSEIN  AHMADI
# https://MrPython.blog.ir
###########################



function check()
{
	if (( "$?" != 0 ))
	then
		echo "There is Some problems !"
		exit 1
	fi
}
user=$(id -u)

if (( $user != 0 ))
then
	echo "Please Run With Sudo :)";
	exit 1;
fi


chmod +x ./libs/change_firmware.sh
echo "Installing ...";
apt update;
check
apt install dfu-programmer -y
check
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=/usr/bin sh
check
arduino-cli config init
check
arduino-cli core update-index
check
arduino-cli board listall uno
check
arduino-cli core install arduino:avr
check

echo "Ok ! your Uno2Rubber Is Ready ... Enjoy :)";
