#!/usr/bin/python3
"""This module defines a class to manage storage of hbnb models"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models"""

    __file_path = "file.json"
    __objects = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def __init__(self):
        """Create a dictionary"""
        self.reload()

    def reload(self):
        """Deserialize the JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value["__class__"]
                    obj = FileStorage.__objects[cls_name](**value)
                    FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(data, f)

    def classes(self):
        """Return a dictionary of class names and their corresponding classes"""
        return FileStorage.__objects

    def all(self, cls=None):
        """Return a dictionary of objects of a specific class or all classes"""
        if cls is None:
            return FileStorage.__objects
        else:
            return {key: obj for key, obj in FileStorage.__objects.items() if isinstance(obj, cls)}

    def count(self, cls=None):
        """Return the count of objects of a specific class or all classes"""
        if cls is None:
            return len(FileStorage.__objects)
        else:
            return len(self.all(cls))

    def show(self, cls, id):
        """Return the object with the given ID from a specific class"""
        key = "{}.{}".format(cls, id)
        return FileStorage.__objects.get(key, None)

    def destroy(self, cls, id):
        """Delete an object with the given ID from a specific class"""
        key = "{}.{}".format(cls, id)
        obj = FileStorage.__objects.get(key, None)
        if obj:
            del FileStorage.__objects[key]
            self.save()

    def update(self, cls, id, attr_name, attr_value):
        """Update an object's attribute with the given value"""
        key = "{}.{}".format(cls, id)
        obj = FileStorage.__objects.get(key, None)
        if obj:
            setattr(obj, attr_name, attr_value)
            self.save()

