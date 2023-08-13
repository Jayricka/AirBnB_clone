#!/usr/bin/python3
"""Console module"""

import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """Create a new instance of BaseModel and saves it to JSON file"""
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args.split()[0]
            class_obj = eval(class_name)
            new_instance = class_obj()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = storage.all()
        if key in objects:
            if len(args_list) < 4:
                print("** attribute name missing **")
                return
            if len(args_list) < 5:
                print("** value missing **")
                return
            attr_name = args_list[3]
            attr_value = args_list[4]
            obj = objects[key]
            try:
                attr_value = eval(attr_value)
            except:
                pass
            setattr(obj, attr_name, attr_value)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representations of instances"""
        args_list = args.split()
        objects = storage.all()
        if not args_list:
            print([str(obj) for obj in objects.values()])
        else:
            if args_list[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in objects.items() if args_list[0] in key])

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles EOF signal to exit the program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
