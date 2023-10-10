#!/usr/bin/python3
""" Converts from python to json and from json to python. """
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """ Converts python to json and other way. """
    __file_path = 'file.json'
    __objects = {} #className.id

    def all(self):
        """ returns a dic (__objects). """
        return FileStorage.__objects

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

    def reload(self):
        """ Deserializes the json file to __objects only of the json file
            exists: otherwise, do nothing if the file doesn't exist, no 
            exception should be raised. """
        classes = {'BaseModel': BaseModel}
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as file:
            data = None

            data = json.load(file)

            if data is None:
                return

            FileStorage.__objects = {
                key: classes[key.split('.')[0]](**value)
                for key, value in data.items()}
