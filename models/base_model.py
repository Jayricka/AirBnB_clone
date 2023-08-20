#!/usr/bin/python3
"""This module defines the BaseModel class."""

import uuid
from datetime import datetime
import models

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

    def save(self):
        """Save the current instance's data to the storage engine."""
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Remove the current instance's data from the storage engine."""
        models.storage.delete(self)

    @classmethod
    def all(cls):
        """Return a dictionary of all instances."""
        return models.storage.all(cls)

    @classmethod
    def count(cls):
        """Return the number of instances in storage."""
        return models.storage.count(cls)

    @classmethod
    def find_by_id(cls, id):
        """Find an instance by its ID."""
        return models.storage.find(cls, id)

    @classmethod
    def find(cls, **kwargs):
        """Find instances that match the given criteria."""
        return models.storage.find(cls, **kwargs)

if __name__ == "__main__":
    pass

