#!/usr/bin/python3
""" Serialization and desarialization JSON """

import json
from models.base_model import BaseModel

class FileStorage:
    """ Serializes instances to a JSON file 
        and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary """
        return(self.__objects)

    def new(self, obj):
        """ Sets in __objects the obj with key """
        k_dict = obj.__class__.__name__ + "." + obj.id
        self.__objects[k_dict] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        j_obj = {}
        for key_dict in self.__objects:
            j_obj[key_dict] = self.__objects[key_dict].to_dict()
        with open(self.__file_path, "w") as op_r:
            json.dump(j_obj, op_r)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path) as op_r:
                self.__objects = json.loads(file.read())

        except:
           pass

