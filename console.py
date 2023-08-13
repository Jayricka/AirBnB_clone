#!/usr/bin/python3
"""This module defines the HBNBCommand class."""

import cmd
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """This class defines the command line interpreter for HBNB."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
            instance = cls()
            instance.save()
            print(instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls, obj_id = arg.split(" ")
            objs = storage.all()
            key = "{}.{}".format(cls, obj_id)
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")
        except:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls, obj_id = arg.split(" ")
            objs = storage.all()
            key = "{}.{}".format(cls, obj_id)
            if key in objs:
                objs.pop(key)
                storage.save()
            else:
                print("** no instance found **")
        except:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            objs = storage.all()
            print([str(obj) for obj in objs.values()])
        else:
            try:
                cls = eval(arg)
                objs = storage.all()
                filtered_objs = [str(obj) for key, obj in objs.items() if isinstance(obj, cls)]
                print(filtered_objs)
            except:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            parts = arg.split(" ")
            cls_name = parts[0]
            obj_id = parts[1]
            key = "{}.{}".format(cls_name, obj_id)
            objs = storage.all()
            if key not in objs:
                print("** no instance found **")
                return
            if len(parts) < 3:
                print("** attribute name missing **")
                return
            if len(parts) < 4:
                print("** value missing **")
                return
            attr_name = parts[2]
            attr_value = parts[3].strip('"')
            setattr(objs[key], attr_name, attr_value)
            objs[key].save()
        except:
            print("** instance id missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

