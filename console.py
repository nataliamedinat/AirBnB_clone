#!/usr/bin/python3
""" Console """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Console for AirBnb
 """
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ End of file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        raise SystemExit

    def quit_help(self):
        print("Quit command to exit the program")

    def emptyline(self):
        """ Empty line entered, don´t execute nothing """
        pass


console = HBNBCommand()
console.cmdloop()
