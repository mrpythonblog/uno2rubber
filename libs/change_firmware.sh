#!/bin/bash
firmware=$1
micro=$2
clear
echo ":: Change Firmware Of Board ::"
echo "-------------------------------"
dfu-programmer $micro get &> /dev/null
while (( $? != 0 ))
do
  sleep 1
  clear
  echo "Please Reset Arduino"
  dfu-programmer $micro get &> /dev/null

done
echo "OK"
echo "Please Wait ..."
sleep 5
echo "Erase ..."
dfu-programmer $micro erase
echo "Flashing Firmware ..."
dfu-programmer $micro flash $firmware
echo "Reset ..."
dfu-programmer $micro reset
if (( $? == 0 ))
then
  echo "Done !"
  exit 0
else
  echo "There is Some Problems :(" 2>&1
  exit 1
fi
