# Uno2Rubber :)

Uno2Rubber , is a tool that automates the process of converting an Arduino UNO (R3) to a Rubber Ducky (for windows systems).

you can run a custom BatchFile (.bat file) on the target using this Rubber Ducky

by default , the Uno boards can't support the HID Classes . so we can't make a RubberDucky using that . but this tool can solve this problem .
uno2rubber changes the standard firmware of your Uno board . so your board can act as a RubberDucky .

but after changing the standard firmware of your board , you can't use from your Uno borad for making your normal projects . 
uno2rubber can flash standard firmware of your board , so you can making your normal projects :) 

----------HOW TO USE------------------

1 - install uno2rubber . run -> "chmod +x configure.sh ; sudo ./configure.sh"

2 - Execute Script -> "python3 uno2rubber.py"

3 - you can select your custom option in script . Enjoy :)


---------------NOTES------------------

* This script has tested on the Arduino Uno R3 
* This RubberDucky only works on Windows Systems (7,8,10)
