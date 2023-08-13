#!/usr/bin/python3
"""This module defines the HBNBCommand class."""
import shlex
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand:
    """Simple command processor example."""

    def __init__(self, stdin=None, stdout=None):
        self.stdout = stdout if stdout else sys.stdout
        self.is_interactive = True
        if not sys.stdin.isatty():
            self.is_interactive = False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        if self.is_interactive:
            return True
        else:
            return False

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        parts = shlex.split(line)
        if parts:
            command = parts[0]
            if command == "help":
                print("Documented commands (type help <topic>):")
                print("========================================")
                print("help  quit  create  show  destroy  all  update")
            else:
                print("*** Unknown syntax: {}".format(command))

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to JSON file, and print its id."""
        if len(arg) == 0:
            print("** class name missing **")
            return
        class_name = arg[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        new_instance = storage.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and id."""
        if len(arg) == 0:
            print("** class name missing **")
            return
        class_name = arg[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        instance_id = arg[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        if len(arg) == 0:
            print("** class name missing **")
            return
        class_name = arg[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        instance_id = arg[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.all().pop(key)
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based on the class name or all classes."""
        if len(arg) == 0:
            instance_list = []
            for key in storage.all():
                instance_list.append(str(storage.all()[key]))
            print(instance_list)
            return
        class_name = arg[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        instance_list = []
        for key in storage.all():
            if key.split('.')[0] == class_name:
                instance_list.append(str(storage.all()[key]))
        print(instance_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attributes."""
        if len(arg) == 0:
            print("** class name missing **")
            return
        class_name = arg[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        instance_id = arg[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(arg) < 3:
            print("** attribute name missing **")
            return
        attribute_name = arg[2]
        if len(arg) < 4:
            print("** value missing **")
            return
        attribute_value = arg[3]
        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def run(self):
        """Run the command processor"""
        if self.is_interactive:
            print("(hbnb)")
            while True:
                line = input("(hbnb) ")
                if line == "quit":
                    break
                self.onecmd(line)
        else:
            input_lines = sys.stdin.read().splitlines()
            for line in input_lines:
                self.onecmd(line)
                self.stdout.write("(hbnb)\n")
                self.stdout.flush()

    def onecmd(self, line):
        """Process a single command"""
        parts = shlex.split(line)
        if parts:
            cmd = "do_" + parts[0]
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func(parts)
            else:
                self.default(line)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-c":
        hbnb = HBNBCommand(stdout=sys.stdout)
        hbnb.run()
    elif not sys.stdin.isatty():
        input_lines = sys.stdin.read().splitlines()
        hbnb = HBNBCommand(stdout=sys.stdout)
        for line in input_lines:
            hbnb.onecmd(line)
            print("(hbnb)")
    else:
        hbnb = HBNBCommand(stdout=sys.stdout)
        hbnb.run()


if __name__ == '__main__':
    main()
