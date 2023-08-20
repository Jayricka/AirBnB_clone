#!/usr/bin/python3
"""This module contains the command line interpreter for the AirBnB project."""

import cmd
import sys
import json
import uuid
from datetime import datetime
from models import storage, classes  # Import your storage and classes here

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter using Ctrl-D (EOF)"""
        return True

    def do_help(self, arg):
        """Show help"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to JSON file"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key in objects:
                objects.pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        objects = storage.all()
        if not args:
            result = [str(obj) for obj in objects.values()]
            print(result)
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            result = [str(obj) for key, obj in objects.items() if key.split(".")[0] == class_name]
            print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3]
                instance = objects[key]
                try:
                    attr_value = eval(attr_value)  # Cast to the appropriate type
                except:
                    pass
                setattr(instance, attr_name, attr_value)
                instance.save()

def run_interactive():
    HBNBCommand().cmdloop()

def run_non_interactive():
    for line in sys.stdin:
        HBNBCommand().onecmd(line.strip())

if __name__ == '__main__':
    if len(sys.argv) == 1:
        run_interactive()
    else:
        run_non_interactive()
