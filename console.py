#!/usr/bin/python3
"""Console module"""

import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

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
        if args_list[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = models.storage.all()
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
        if args_list[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = models.storage.all()
        if key in objects:
            del objects[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_update(self, args):
        """Updates an instance based on the class name and id with a dictionary"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
        if args_list[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = models.storage.all()
        if key in objects:
            if len(args_list) < 3:
                print("** attribute name missing **")
                return
            if len(args_list) < 4:
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
            models.storage.save()
        else:
            print("** no instance found **")

    def do_update_with_dict(self, args):
        """Updates an instance by its ID with a dictionary representation"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
        if args_list[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = models.storage.all()
        if key in objects:
            if len(args_list) < 3:
                print("** dictionary missing **")
                return
            try:
                dictionary = eval(args_list[2])
            except:
                print("** invalid dictionary format **")
                return
            obj = objects[key]
            for attr_name, attr_value in dictionary.items():
                setattr(obj, attr_name, attr_value)
            models.storage.save()
        else:
            print("** no instance found **")

    def do_count(self, args):
        """Retrieves the number of instances of a class"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
        if args_list[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        count = 0
        objects = models.storage.all()
        for key in objects:
            class_name = key.split('.')[0]
            if class_name == args_list[0]:
                count += 1
        print(count)

    def do_EOF(self, args):
        """Handles EOF signal to exit the program"""
        print()
        return True

    def emptyline(self):
        """Handles an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

