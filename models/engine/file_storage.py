#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json
from models.base_model import BaseModel

class FileStorage:
    """This class defines methods to serialize/deserialize objects."""

    __file_path = "file.json"
    __objects = {}
    classes = []  # Add this attribute to store class names

    def all(self, cls=None):
        """Return a list of objects of a specific class or all objects."""
        if cls:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        else:
            return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the file exists)."""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split(".")
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)
                    if cls_name not in self.classes:
                        self.classes.append(cls_name)  # Update the classes list
        except FileNotFoundError:
            pass

