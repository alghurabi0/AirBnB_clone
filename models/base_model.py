#!/usr/bin/python3
""" Base model for other models in this project. """
import models
import uuid
from datetime import datetime


class BaseModel:
    """ Base model for other classes. """
    def __init__(self, *args, **kwargs):
        """ Initilization of the instance. """
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']

            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    strp = datetime.strptime
                    setattr(self, key, strp(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
            if hasattr(self, 'created_at') is False:
                self.created_at = datetime.now()
            if hasattr(self, 'updated_at') is False:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ updated the instance. """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary of attributes. """
        obj_dict = self.__dict__.copy()
        for key, value in obj_dict.items():
            if isinstance(value, datetime):
                obj_dict[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """ formats how print works. """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )
    @classmethod
    def all(cls):
        """
        Return a dict of all instance of the class.
        """
        return storage.all(cls.__name__)
