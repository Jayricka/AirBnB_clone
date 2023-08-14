#!/usr/bin/env python3
"""Unit tests for Amenity class."""

import unittest
from models.amenity import Amenity
from datetime import datetime

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_constructor(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_amenity_str(self):
        amenity_str = str(self.amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn("id", amenity_str)
        self.assertIn("created_at", amenity_str)
        self.assertIn("updated_at", amenity_str)

    def test_amenity_save(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_amenity_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_amenity_custom_attributes(self):
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_amenity_update_attributes(self):
        old_created_at = self.amenity.created_at
        self.amenity.update(name="Gym")
        self.assertEqual(self.amenity.name, "Gym")
        self.assertNotEqual(old_created_at, self.amenity.created_at)

    def test_amenity_str_representation(self):
        self.amenity.name = "Gym"
        amenity_str = str(self.amenity)
        self.assertIn("[Amenity] ({})".format(self.amenity.id), amenity_str)
        self.assertIn("'name': 'Gym'", amenity_str)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
