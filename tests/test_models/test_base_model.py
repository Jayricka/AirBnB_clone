#!/usr/bin/python3
"""Unittests for BaseModel class."""

import unittest
from models.base_model import BaseModel
from models import storage  # Import the storage module

class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for BaseModel class instantiation."""

    def test_new_instance_stored_in_objects(self):
        """Test that new BaseModel instance is stored in __objects."""
        bm = BaseModel()
        key = "{}.{}".format(type(bm).__name__, bm.id)
        self.assertIn(key, storage.all())

if __name__ == "__main__":
    unittest.main()
