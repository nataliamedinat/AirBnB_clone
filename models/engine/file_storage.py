#!/usr/bin/python3
""" Serialization and desarialization JSON """


class FileStorage(self):
    """ Serializes instances to a JSON file 
        and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary """
        return(self.__objects)

    def new(self, obj):
        """ Sets in __objects the obj with key """
        obj_dict = obj.to_dict()
        k_dict = obj_dict["__class"] + '.' + obj_dict["id"]
        self.__objects[] = obj_dict

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(file) as op_r:
        op_r = json.dumps(self.__objects)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:

        except:

