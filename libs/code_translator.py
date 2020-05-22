class code_translator:
    keys = {"!" : "0x1e" , "@" : "0x1f" , "#" : "0x20" , "$" : "0x21" , "%" : "0x22" , "^" : "0x23" , "&" : "0x24" , "*" : "0x25" , "(" : "0x26",
    ")" : "0x27","-" : "0x2d" , "_" : "0x2d", "=" : "0x2e" , "+" : "0x2e" , "\\" : "0x31" , "|" : "0x31" , "~" : "0x35" , "`" : "0x35", "/" : "0x38" , "?" : "0x38",
    "." : "0x37" , ">" : "0x37" , "," : "0x36" , "<" : "0x36", ";" : "0x33" , ":" : "0x33" , "\"" : "0x34" , "'" : "0x34"}
    def __init__(self,command):
        self.command = command.replace("\n"," & ")
        self.translate()
    def translate(self):
        output = ""
        strings = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        symbols_shift = "!@#$%^&*()_+|~?\":<>"
        symbols_nonshift = "-\\=`/.,;'"
        cm = self.command
        for item in cm:
            if item in strings:
                output += '\nkeyString("{}");'.format(item)
            elif item in symbols_shift:
                output += "\nkeyPress(LEFT_SHIFT,{});\nkeyRelease();".format(self.keys[item])
            elif item in symbols_nonshift:
                output += "\nkeyPress(0,{});\nkeyRelease();".format(self.keys[item])
        self.output = output
        return 0
