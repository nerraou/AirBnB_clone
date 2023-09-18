#!/usr/bin/python3
"""The entry point of the command interpreter"""


import cmd
from models import storage
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This is Hbnb class; console managment"""
    prompt = '(hbnb) '
    # Place, State, City, Amenity and Review
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
    }

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
        if attribute in obj.__dict__:
            try:
                currentValue = getattr(obj, attribute)
                obj_type = type(currentValue)
                value = obj_type(value)
            except Exception:
                return False
        setattr(obj, attribute, value)
        storage.save()

    def default(self, arg):
        """override default method"""
        pattern = "([a-zA-Z]+)\\.([a-zA-Z]+)\\((?:\\\"([^\\\"]*)\\\")?\\)"
        matches = re.match(pattern, arg)

        if matches is None:
            print("*** Unknown syntax:", arg)
            return False

        groups = matches.groups()
        actions_dict = {
            "all": lambda: self.print_all(groups[0]),
            "count": lambda: self.print_count(groups[0]),
            "show": lambda: self.show_instance(groups[0], groups[2]),
            "destroy": lambda: self.destroy_instance(groups[0], groups[2]),
        }

        if groups[1] in actions_dict:
            actions_dict[groups[1]]()
        else:
            print("*** Unknown syntax:", arg)
            return False

    def print_all(self, entity):
        """print all of entity"""
        objects = storage.all()
        array = []
        for key in objects:
            obj = objects[key]
            if obj.__class__.__name__ == entity:
                array.append(str(obj))
        print(array)

    def print_count(self, entity):
        """print entity count"""
        count = 0
        objects = storage.all()
        for key in objects:
            obj = objects[key]
            if obj.__class__.__name__ == entity:
                count += 1
        print(count)

    def show_instance(self, entity, id):
        """show instance by id"""
        objects = storage.all()
        key = "{}.{}".format(entity, id)

        if key not in objects:
            print("** no instance found **")
            return False

        print(objects[key])

    def destroy_instance(self, entity, id):
        """destroy instance by id"""
        objects = storage.all()
        key = "{}.{}".format(entity, id)

        if key not in objects:
            print("** no instance found **")
            return False

        objects.pop(key)
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
