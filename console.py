#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line does nothing"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
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
        """Show the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key, None)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key, None)
            if obj:
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all instances or all instances of a class"""
        args = arg.split()
        obj_list = []
        if not arg:
            for key, obj in storage.all().items():
                obj_list.append(str(obj))
            print(obj_list)
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key, None)
            if obj:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    setattr(obj, args[2], args[3])
                    storage.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Count the number of instances of a class"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            count = 0
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    count += 1
            print(count)

    def default(self, line):
        """Handle default command"""
        args = line.split('.')
        if len(args) >= 2:
            if args[0] in storage.classes():
                if args[1] == "all()":
                    self.do_all(args[0])
                elif args[1] == "count()":
                    self.do_count(args[0])
                elif args[1][:5] == "show(":
                    arg = args[1][5:-1]
                    self.do_show(args[0] + ' ' + arg)
                elif args[1][:8] == "destroy(":
                    arg = args[1][8:-1]
                    self.do_destroy(args[0] + ' ' + arg)
                elif args[1][:7] == "update(":
                    arg = args[1][7:]
                    self.do_update(args[0] + ' ' + arg)
                elif args[1][:6] == "create":
                    self.do_create(args[0])
                elif args[1][:3] == "new":
                    self.do_create(args[0])
                else:
                    print("** invalid syntax **")
            else:
                print("** class doesn't exist **")
        else:
            print("** invalid syntax **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

