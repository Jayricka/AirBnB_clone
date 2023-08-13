#!/usr/bin/python3
"""This module defines the HBNBCommand class."""
import shlex
import sys
from models.base_model import BaseModel

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
                print("help  quit")
            else:
                print("*** Unknown syntax: {}".format(command))

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

