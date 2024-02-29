#!/usr/bin/python3
"""Module that defines a command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """exit the program with (ctrl+D)"""
        print("")
        return True

    def help_EOF(self):
        print("Exit the program when EOF is reached (Ctrl+D)")

    def emptyline(self):
        """do nothing when press enter and no command"""
        pass

    def do_create(self, arg):
        """create a new instance of BaseModel save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """print the string of a instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class d0oesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        object = storage.all()
        if key in object:
            print(object[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print string representation of all instances"""
        args = shlex.split(arg)
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                cls = eval(args[0])
                print([str(obj) for key, obj in objects.items()
                       if key.split('.')[0] == args[0]])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass
        setattr(objects[key], attribute_name, attribute_value)
        objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
