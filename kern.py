import * from _Barnacle_buster, curses


class egress:

    def __init__(self):
        name = Operation System
        while True:#feel like this should be wit the curses module
            indown(text = input('CmdPmt>'))
            print(indown(text))


    def indown(self):#I gotta make a window and somehow have that while loop be my line where u ttype
        scr = curses.init()
        scr.refresh()
        scr.noecho()
        scr.cbreak(False)
        scr.def_shell_mode()
        
        
        
