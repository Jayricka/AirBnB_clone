from datetime import datetime
from models.base_model import BaseModel
import models

class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize the Place instance."""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return a string representation of the Place instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute current datetime."""
        from models import storage  # Import storage here
        self.updated_at = datetime.now()
        storage.save()  # Call the save method from the storage instance

    def to_dict(self):
        """Return a dictionary representation of the Place instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

