#!/usr/bin/env python3
"""Unit tests for State class."""

import unittest
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_state_constructor(self):
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_state_str(self):
        state_str = str(self.state)
        self.assertIn("[State]", state_str)
        self.assertIn("id", state_str)
        self.assertIn("created_at", state_str)
        self.assertIn("updated_at", state_str)

    def test_state_save(self):
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_state_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_state_custom_attributes(self):
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_state_update_attributes(self):
        old_created_at = self.state.created_at
        self.state.update(name="New York")
        self.assertEqual(self.state.name, "New York")
        self.assertNotEqual(old_created_at, self.state.created_at)

    def test_state_str_representation(self):
        self.state.name = "Washington"
        state_str = str(self.state)
        self.assertIn("[State] ({})".format(self.state.id), state_str)
        self.assertIn("'name': 'Washington'", state_str)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()

