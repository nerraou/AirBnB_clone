#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """This is Hbnb class; console managment"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
