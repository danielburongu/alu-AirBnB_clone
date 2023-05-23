#!/usr/bin/python3
import json
import os
"""File Storage module. Currently to JSON files"""


class FileStorage:
    """Serialize into JSON file"""

    __file_path = "./file.json"
    __objects = {}

    def __init__(self):
        """Init"""
        pass

    def destroy(self, objid):
        """Destroy the object in the json file"""
        for k, v in type(self).__objects.items():
            if k.split(".")[-1] == objid:
                del type(self).__objects[k]
                return

    def all(self):
        """Return all objects in dict form"""
        return type(self).__objects

    def new(self, obj):
        """Add a new object into the dict"""
        name = type(obj).__name__
        type(self).__objects[name + "." + str(obj.id)] = obj

    def save(self):
        """Save all objects in the dict into a file"""
        tempdict = {k: v.to_dict() for k, v in type(self).__objects.items()}
        with open(type(self).__file_path, "w+") as f:
            json.dump(tempdict, f)

    def reload(self):
        """Reload all objects from a file into the dict"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path) as f:
                tempdict = json.load(f)
            for k, v in tempdict.items():
                classn = v["__class__"]
                type(self).__objects[k] = eval(classn + "(**v)")
