#!/usr/bin/python3
"""This module defines a User class that inherits from BaseModel."""
from models.base_model import BaseModel

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

# To avoid circular import issues during deserialization
# between User and BaseModel, we import BaseModel at the end.
from models import storage

