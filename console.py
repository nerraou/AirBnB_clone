#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd
from models import storage
import re
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """This is Hbnb class; console managment"""
    prompt = '(hbnb) '

    __classes = {"BaseModel": BaseModel, "User": User}

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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(" ")

        if len(args[0]) == 0:
            print("** class name missing **")
            return False

        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])

        if key not in objects:
            print("** no instance found **")
            return False
        objects.pop(key)
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of
          all instances based or not on the class name."""
        objects = storage.all()
        if len(arg) == 0:
            array = []
            for key in objects:
                array.append(str(objects[key]))
            print(array)
        else:
            if arg not in self.__classes:
                print("** class doesn't exist **")
                return False
            array = []
            for key in objects:
                obj = objects[key]
                if obj.__class__.__name__ == arg:
                    array.append(str(obj))
            print(array)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
            by adding or updating attribute"""
        args = parse(arg)

        if len(args[0]) == 0:
            print("** class name missing **")
            return False

        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])

        if key not in objects:
            print("** no instance found **")
            return False

        if len(args) < 3:
            print("** attribute name missing **")
            return False

        if len(args) < 4:
            print("** value missing **")
            return False
        attribute = args[2]
        value = args[3]
        obj = objects[key]
        currentValue = getattr(obj, attribute)
        obj_type = type(currentValue)
        setattr(obj, attribute, obj_type(value))
        storage.save()


def parse(arg):
    """parse command line argument"""
    args = arg.split(" ")

    if len(args) >= 4 and args[3][0] == '"':
        start_index = arg.find('"')
        end_index = arg.find('"', start_index + 1)
        args[3] = arg[start_index + 1:end_index]
    return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()
