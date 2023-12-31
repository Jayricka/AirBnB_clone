#!/usr/bin/python3
"""State module"""

from models.base_model import BaseModel
from datetime import datetime


class State(BaseModel):
    """State class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return string representation of State."""
        return "[State] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary representation of the State instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
