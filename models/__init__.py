#!/usr/bin/python3
"""This module contains the initialization for the models package."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

# Import your classes here
from models.base_model import BaseModel
from models.user import User
# Add more imports for other classes

# Create a dictionary of class names to classes
classes = {
    "BaseModel": BaseModel,
    "User": User,
    # Add more entries for other classes
}

