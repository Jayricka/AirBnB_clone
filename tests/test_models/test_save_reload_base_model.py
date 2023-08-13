import os
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()  # Save the new object
print(my_model)

# Ensure the object is saved to file.json
storage.save()

# Construct the absolute path to file.json using os.path.join
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../file.json")

# Print the contents of file.json
with open(file_path, "r") as json_file:
    print(json_file.read())

