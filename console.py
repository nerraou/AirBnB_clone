#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is Hbnb class; console managment"""
    prompt = '(hbnb) '

    __classes = {"BaseModel": BaseModel}

    def emptyline(self):
        """Do nothing"""
        pass

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel and print it Id"""
        if not arg:
            print("** class name missing **")
            return False

        if arg not in self.__classes:
            print("** class doesn't exist **")
            return False

        targetClass = self.__classes[arg]
        instance = targetClass()
        instance.save()
        print("{}".format(instance.id))

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id"""
        args = arg.split(" ")

        if len(args[0]) == 0:
            print("** class name missing **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return False

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])

        if key not in objects:
            print("** no instance found **")
            return False

        print(objects[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
