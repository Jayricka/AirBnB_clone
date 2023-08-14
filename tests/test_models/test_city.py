#!/usr/bin/python3
"""City module"""

from models.base_model import BaseModel
from models import storage  # Import storage from models package
from datetime import datetime  # Import datetime module

class City(BaseModel):
    """City class that inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the City instance."""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return a string representation of the City instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute current datetime."""
        self.updated_at = datetime.now()
        storage.save()  # Call the save method from the storage instance

    def to_dict(self):
        """Return a dictionary representation of the City instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

