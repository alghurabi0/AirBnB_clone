#!/usr/bin/python3
""" Converts from python to json and from json to python. """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """ Converts python to json and other way. """
    __file_path = 'file.json'
    __objects = {}
    classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'Amenity': Amenity,
                'Review': Review,
                'State': State,
                'City': City
                }

    def all(self):
        """ returns a dic (__objects). """
        return self.__objects

    def new(self, obj):
        """ sets in (__objects) the obj with key (obj-class-name).id. """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the json file path. """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)
            file.write('\n')

    def reload(self):
        """ Deserializes the json file to __objects only of the json file
            exists: otherwise, do nothing if the file doesn't exist, no
            exception should be raised. """
        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'Amenity': Amenity,
                'Review': Review,
                'State': State,
                'City': City
                }
        if not os.path.exists(FileStorage.__file_path):
            return

        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = None

                data = json.load(file)

                if data is None:
                    return

                FileStorage.__objects = {
                    key: classes[key.split('.')[0]](**value)
                    for key, value in data.items()}
        except Exception:
            pass
