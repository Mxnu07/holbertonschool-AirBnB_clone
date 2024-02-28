#!/usr/bin/python3
"""Module that defines a command interpreter"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
