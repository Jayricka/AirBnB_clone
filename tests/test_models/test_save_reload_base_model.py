#!/usr/bin/python3
import sys
sys.path.append('/home/ricka-g/AirBnB_clone')  # Add this line to set the Python path

from models import storage
from models.base_model import BaseModel

# Retrieve all objects from storage
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Create a new BaseModel instance
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

# Retrieve all objects again to show the newly created object
all_objs = storage.all()
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
