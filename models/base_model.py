#!/usr/bin/python3
"""This module defines the BaseModel class."""
import uuid
from datetime import datetime

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
            self.id = str(uuid.uuid4())  # Generate a unique ID using uuid4 and convert to a string
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

