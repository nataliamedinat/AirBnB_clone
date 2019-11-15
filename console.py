#!/usr/bin/python3
""" Console """

import cmd
from models import classes
import json
from models.engine import file_storage
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """ Console for AirBnb
 """
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ End of file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        raise SystemExit

    def quit_help(self):
        print("Quit command to exit the program")

    def emptyline(self):
        """ Empty line entered, don´t execute nothing """
        pass

    def do_create(self, args):
        """ Creates a new instance, saves it(to the JSON file)
            and prints the id """
        split_args = shlex.split(args)
        if not (args):
            print("** class name missing **")
            return

        try:
            exs_clss = classes[args]
        except Exception:
            print("** class doesn't exist **")
            return
        else:
            instance = classes[args]()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """ Prints str representation of an instance """
        split_args = shlex.split(args)

        if not (args):
            print("** class name missing **")
            return
        try:
            exs_clss = classes[split_args[0]]
        except Exception:
            print("** class doesn't exist **")
            return
        try:
            split_args[1]
        except Exception:
            print("** instance id missing **")
            return

        key = split_args[0] + "." + split_args[1]
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class and id """
        split_args = shlex.split(args)
        if not (args):
            print("** class name missing **")
            return
        try:
            exs_clss = classes[split_args[0]]
        except Exception:
            print("** class doesn't exist **")
            return
        try:
            split_args[1]
        except Exception:
            print("** instance id missing **")
            return
        key = split_args[0] + "." + split_args[1]
        if key in models.storage.all():
            del models.storage.all()[key]
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints all str representation of all instances """
        split_args = shlex.split(args)
        n_list = []
        dict_json = models.storage.all()
        if args:
            try:
                for key in models.storage.all():
                    if split_args[0] == key.split('.')[0]:
                        n_list.append(str(dict_json[key]))
                print(n_list)
            except Exception:
                print("** class doesn't exist **")
        else:
            for key in models.storage.all():
                n_list.append(str(models.storage.all()[key]))
            print(n_list)

    def do_update(self, args):
        """ Updates an instance based on the class name and id """
        split_arg = shlex.split(args)
        if len(split_arg) == 0:
            print("** class name missing **")
            return False
        if split_arg[0] in options:
            if len(split_arg) > 1:
                key = split_arg[0] + '.' + split_arg[1]
                if key in models.storage.all():
                    if len(split_arg) > 2:
                        if len(split_arg) > 3:
                            setattr(models.storage.all()[key], split_arg[2], split_arg[3])
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")






console = HBNBCommand()
console.cmdloop()
