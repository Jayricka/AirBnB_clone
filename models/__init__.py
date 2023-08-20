#!/usr/bin/python3
"""This module contains the initialization for the models package."""

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage to manage serialization and deserialization
storage = FileStorage()

# Load previously serialized data from the JSON file, if it exists
storage.reload()

# Import all your classes here
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Create a dictionary of class names to classes
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
    # Add more entries for other classes as needed
}

