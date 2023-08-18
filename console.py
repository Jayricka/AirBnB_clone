#!/usr/bin/python3
"""Console module"""

import cmd
import sys
import models

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]

    def do_create(self, args):
        """Create a new instance of BaseModel and save to JSON file"""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in self.valid_classes:
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
        if args_list[0] not in self.valid_classes:
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

    def do_all(self, args):
        """Prints all string representations of instances"""
        args_list = args.split()
        objects = models.storage.all()
        if not args_list:
            print([str(obj) for obj in objects.values()])
        else:
            class_name = args_list[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in objects.items() if class_name in key])

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in self.valid_classes:
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
            attr_name = args_list[2]
            attr_value = args_list[3]
            obj = objects[key]
            try:
                attr_value = eval(attr_value)
            except:
                pass
            setattr(obj, attr_name, attr_value)
            models.storage.save()
        else:
            print("** no instance found **")

    def do_count(self, args):
        """Retrieves the number of instances of a class"""
        class_name = args.split()[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        count = 0
        objects = models.storage.all()
        for obj in objects.values():
            if obj.__class__.__name__ == class_name:
                count += 1
        print(count)

    def do_update_with_dict(self, args):
        """Updates an instance based on its ID with a dictionary representation"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return
        class_name = args_list[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args_list[1])
        objects = models.storage.all()
        if key in objects:
            if len(args_list) < 3:
                print("** dictionary missing **")
                return
            try:
                dict_str = " ".join(args_list[2:])
                update_dict = eval(dict_str)
            except:
                print("** invalid dictionary **")
                return
            obj = objects[key]
            for key, value in update_dict.items():
                setattr(obj, key, value)
            obj.save()
        else:
            print("** no instance found **")

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles EOF signal to exit the program"""
        print()
        return True

    def emptyline(self):
        """Handles empty line"""
        pass

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-c":
        # Non-interactive mode (reading from stdin)
        lines = sys.stdin.read().splitlines()
        for line in lines:
            if line:
                print("(hbnb)")
                print(line)
                HBNBCommand().onecmd(line)
    else:
        # Interactive mode
        HBNBCommand().cmdloop()

if __name__ == '__main__':
    main()

