from datetime import datetime
from models.base_model import BaseModel
import models


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Amenity instance."""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return a string representation of the Amenity instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute current datetime."""
        from models import storage  # Import storage here
        self.updated_at = datetime.now()
        storage.save()  # Call the save method from the storage instance

    def to_dict(self):
        """Return a dictionary representation of the Amenity instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
