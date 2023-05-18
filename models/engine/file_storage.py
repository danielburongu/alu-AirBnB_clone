#!/usr/bin/python3
"""first user file storage"""

import json

class FileStorage:
    # Existing code...

    def serialize(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def deserialize(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
