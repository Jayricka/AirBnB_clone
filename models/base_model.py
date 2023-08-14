#!/usr/bin/python3
"""This module defines the BaseModel class."""
import uuid
from datetime import datetime
from models import storage  # Import storage from models package
from uuid import uuid4  # Import uuid4 from the uuid module

class BaseModel:
    """This class defines common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())  # Generate a unique ID using uuid4
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute current datetime."""
        self.updated_at = datetime.now()
        storage.new(self)  # Add the object to the storage instance
        storage.save()     # Call the save method from the storage instance

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
