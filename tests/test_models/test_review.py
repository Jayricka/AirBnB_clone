#!/usr/bin/env python3
"""Unit tests for Review class."""

import unittest
from models.review import Review
from datetime import datetime

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_review_constructor(self):
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_review_str(self):
        review_str = str(self.review)
        self.assertIn("[Review]", review_str)
        self.assertIn("id", review_str)
        self.assertIn("created_at", review_str)
        self.assertIn("updated_at", review_str)

    def test_review_save(self):
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_review_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_review_custom_attributes(self):
        self.review.place_id = "place_123"
        self.assertEqual(self.review.place_id, "place_123")
        self.review.user_id = "user_456"
        self.assertEqual(self.review.user_id, "user_456")
        self.review.text = "Great experience!"
        self.assertEqual(self.review.text, "Great experience!")

    def test_review_update_attributes(self):
        old_created_at = self.review.created_at
        self.review.update(place_id="place_789", text="Updated review")
        self.assertEqual(self.review.place_id, "place_789")
        self.assertEqual(self.review.text, "Updated review")
        self.assertNotEqual(old_created_at, self.review.created_at)

    def test_review_str_representation(self):
        self.review.text = "Amazing place!"
        review_str = str(self.review)
        self.assertIn("[Review] ({})".format(self.review.id), review_str)
        self.assertIn("'text': 'Amazing place!'", review_str)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
