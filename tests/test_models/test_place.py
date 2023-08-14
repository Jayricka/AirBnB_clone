#!/usr/bin/env python3
"""Unit tests for Place class."""

import unittest
from models.place import Place
from datetime import datetime

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_place_constructor(self):
        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_place_str(self):
        place_str = str(self.place)
        self.assertIn("[Place]", place_str)
        self.assertIn("id", place_str)
        self.assertIn("created_at", place_str)
        self.assertIn("updated_at", place_str)

    def test_place_save(self):
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_place_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_place_custom_attributes(self):
        self.place.city_id = "city_123"
        self.assertEqual(self.place.city_id, "city_123")
        self.place.name = "Cozy Cabin"
        self.assertEqual(self.place.name, "Cozy Cabin")

    def test_place_update_attributes(self):
        old_created_at = self.place.created_at
        self.place.update(city_id="city_456", name="Luxury Suite")
        self.assertEqual(self.place.city_id, "city_456")
        self.assertEqual(self.place.name, "Luxury Suite")
        self.assertNotEqual(old_created_at, self.place.created_at)

    def test_place_str_representation(self):
        self.place.name = "Beachfront Villa"
        place_str = str(self.place)
        self.assertIn("[Place] ({})".format(self.place.id), place_str)
        self.assertIn("'name': 'Beachfront Villa'", place_str)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
