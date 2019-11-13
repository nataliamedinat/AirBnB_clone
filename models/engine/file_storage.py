#!/usr/bin/python3
""" Serialization and desarialization JSON """

import json
import models


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
        with open(self.__file_path, "w+") as op_r:
            op_r.write(json.dumps(j_obj))

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path) as op_r:
                """self.__objects = json.load(file.read())"""
                file_str = op_r.read()
                if len(file_str) == 0:
                    return
                receiver = json.loads(op_r.read())
                for key, value in receiver.items():
                    split_class = key.split('.')[0]
                    obj = models.classes[split_class](**value)
                    self.__objects[key] = obj
        except:
            pass
