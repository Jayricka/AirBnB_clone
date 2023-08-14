#!/usr/bin/python3
"""This module defines the FileStorage class for managing serialization and deserialization of objects."""
import json
import os.path

class FileStorage:
    """This class manages serialization and deserialization of objects."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set obj in __objects with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        json_dict = {}
        for key, obj in FileStorage.__objects.items():
            json_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name = value["__class__"]
                    obj = globals()[class_name](**value)  # Create instance of the class
                    FileStorage.__objects[key] = obj
