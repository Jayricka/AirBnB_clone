#!/usr/bin/python3
"""This module defines the FileStorage class for serializing and deserializing objects."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """This class serializes and deserializes objects to and from JSON format."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized = {}
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)."""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                deserialized = json.load(file)
                for key, value in deserialized.items():
                    class_name = value['__class__']
                    if class_name == 'BaseModel':
                        obj = BaseModel(**value)
                    elif class_name == 'User':
                        obj = User(**value)
                    elif class_name == 'Place':
                        obj = Place(**value)
                    elif class_name == 'State':
                        obj = State(**value)
                    elif class_name == 'City':
                        obj = City(**value)
                    elif class_name == 'Amenity':
                        obj = Amenity(**value)
                    elif class_name == 'Review':
                        obj = Review(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

