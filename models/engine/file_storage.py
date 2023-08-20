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
