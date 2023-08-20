#!/usr/bin/python3
"""This is the entry point of the command interpreter."""
import cmd
import models

class HBNBCommand(cmd.Cmd):
    """Cmd class for the command interpreter."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Create a new instance of a specified class."""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
            else:
                try:
                    new_obj = models.classes[class_name]()
                    new_obj.save()
                    print(new_obj.id)
                except Exception as e:
                    print("** {}".format(e))

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                all_objects = models.storage.all()
                if key in all_objects:
                    print(all_objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                all_objects = models.storage.all()
                if key in all_objects:
                    del all_objects[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances."""
        if not arg:
            obj_list = [str(obj) for obj in models.storage.all().values()]
            print(obj_list)
        else:
            class_name = arg
            if class_name not in models.classes:
                print("** class doesn't exist **")
            else:
                obj_list = [str(obj) for obj in models.storage.all().values() if type(obj).__name__ == class_name]
                print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                all_objects = models.storage.all()
                if key not in all_objects:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    instance = all_objects[key]
                    setattr(instance, attr_name, attr_value)
                    instance.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
