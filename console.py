#!/usr/bin/python3
"""This module defines the HBNBCommand class."""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from datetime import datetime
import uuid

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass
    
    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        parts = shlex.split(line)
        if len(parts) == 2 and parts[1][0] == "{" and parts[1][-1] == "}":
            d = eval(parts[1])
            if "__class__" in d:
                class_name = d.pop("__class__")
                instance = eval(class_name)(**d)
                print(instance)
        else:
            print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()

