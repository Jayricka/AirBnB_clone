#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage

class TestSaveReloadBaseModel(unittest.TestCase):
    """Test cases for saving and reloading BaseModel."""
    
    def test_save_reload(self):
        """Test saving and reloading a BaseModel object."""
        # Create a new BaseModel object
        new_base_model = BaseModel()
        new_base_model.name = "My_First_Model"
        new_base_model.my_number = 89
        new_base_model.save()
        
        # Reload objects from storage (simulating a new session)
        storage.reload()
        
        # Verify the reloaded object
        # Construct the correct key for accessing the reloaded object
        key = f"BaseModel.{new_base_model.id}"
        reloaded_base_model = storage.all().get(key)
        
        # Check if the reloaded object is found
        self.assertIsNotNone(reloaded_base_model)
        
        # Compare attributes of the original and reloaded objects
        self.assertEqual(new_base_model.id, reloaded_base_model.id)
        self.assertEqual(new_base_model.created_at, reloaded_base_model.created_at)
        self.assertEqual(new_base_model.updated_at, reloaded_base_model.updated_at)
        self.assertEqual(new_base_model.name, reloaded_base_model.name)
        self.assertEqual(new_base_model.my_number, reloaded_base_model.my_number)

if __name__ == '__main__':
    unittest.main()

