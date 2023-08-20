#!/usr/bin/python3
import sys
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from models import storage
from models.user import User

# Retrieve all objects from storage
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print("[User] ({}) {}".format(my_user.id, my_user.to_dict()))

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print("[User] ({}) {}".format(my_user2.id, my_user2.to_dict()))
