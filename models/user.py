#!/usr/bin/python3
"""This module defines a User class that inherits from BaseModel."""

from models.base_model import BaseModel
from datetime import datetime


class User(BaseModel):
    """Class representing a user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return string representation of User."""
        return "[User] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute current datetime."""
        from models import storage  # Import storage here
        self.updated_at = datetime.now()
        storage.save()  # Call the save method from the storage instance

    def to_dict(self):
        """Return a dictionary representation of the User instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
