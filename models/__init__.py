#!/usr/bin/python3
"""This module initializes the FileStorage instance."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
