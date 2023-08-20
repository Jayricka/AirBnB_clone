#!/usr/bin/python3
"""This module initializes the FileStorage instance."""
from models.engine.file_storage import FileStorage

# Create a global FileStorage instance
storage = FileStorage()

# Load objects from the JSON file, if it exists
storage.reload()
