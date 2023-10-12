#!/usr/bin/python3
""" Console module for devs. """
import cmd
from models.base_model import BaseModel
import json
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Command line cmd. """
    prompt = "(hbnb) "

    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'City': City,
            'State': State,
            'Amenity': Amenity,
            'Review': Review
            }

    """def precmd(self, line):
        Checks before precessing to commands.
        args = line.split(' ')
        if len(args) == 1 and '.' in line:
            args2 = line.split('.')
            if args2[1] == 'all()':
                if args2[0] not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                    return ""
                else:
                    all_instances = storage.all()
                    print([f"{v}" for k, v in
                            all_instances.items() if
                            isinstance(all_instances[k],
                                HBNBCommand.classes[args2[0]])])
                    return ""
            elif args2[1] == 'count()':
                if args2[0] not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                    return ""
                else:
                    all_instances = storage.all()
                    inst_list = [v for k, v in all_instances.items()
                            if isinstance(all_instances[k],
                                HBNBCommand.classes[args2[0]])]
                    print(len(inst_list))
                    return ""
            elif 'show(' in args2[1]:
                if args2[0] not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                    return ""
                else:
                    args_show = line.split('(')
                    show_id = args_show[1].split(')')
                    class_name = args2[0]
                    instance_key = f'{class_name}.{show_id[0]}'
                    if self.find(instance_key) == False:
                        print("** no instance found **")
                        return ""
                    else:
                        all_instances = storage.all()
                        print(all_instances[instance_key])
                        return ""
            else:
                return line
        else:
            return line"""

    @classmethod
    def find(cls, name_id):
        """ finds the instance. """
        all_instances = storage.all()
        if name_id in all_instances:
            return True
        else:
            return False

    def do_quit(self, line):
        """ quits the command line. """
        return True

    def do_EOF(self, line):
        """ Signals EOF to cmd. """
        return True

    def emptyline(self):
        """ empty line don't do anything. """
        pass

    def do_create(self, line):
        """ Creates a new instance of a class and saves it to a json file. """
        args = line.split(' ')
        if args[0] == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) != 1:
            print("invalid arguments")
        else:
            instance = HBNBCommand.classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """ Prints the string representation of an instance based on the
            class name and id, $ show BaseModel 1234-1234-1234. """
        args = line.split(' ')
        if args[0] == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instnce id missing **')
        elif len(args) > 2:
            print('** invalid arguments **')
        else:
            class_name = args[0]
            instance_id = args[1]
            instance_key = f'{class_name}.{instance_id}'
            if self.find(instance_key) is False:
                print('** no instance found **')
            else:
                all_instances = storage.all()
                print(all_instances[instance_key])

    def do_destroy(self, line):
        """ destroys an instance and saves the changes to the json file. """
        args = line.split(' ')
        if args[0] == "":
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instnce id missing **')
        elif len(args) > 2:
            print('** invalid arguments **')
        else:
            class_name = args[0]
            instance_id = args[1]
            instance_key = f'{class_name}.{instance_id}'
            all_instances = storage.all()
            if self.find(instance_key) is False:
                print('** no instance found **')
            else:
                del all_instances[instance_key]
                storage.save()

    def do_all(self, line):
        """ Print string repr of all instances. """
        args = line.split(' ')
        if args[0] == "":
            all_instances = storage.all()
            print(["{}".format(str(v)) for k, v in all_instances.items()])
        elif len(args) != 1:
            print("invalid arguments")
        else:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                all_in = storage.all()
                print([
                    "{}".format(str(v)) for v in all_in.values()
                    if v.__class__.__name__ == args[0]])

    @classmethod
    def isfloat(cls, value):
        """ checks if value is float."""
        try:
            float(value)
            return True
        except ValueError:
            return False

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". """
        args = line.split(' ')
        if args[0] == "":
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        elif self.find(f'{args[0]}.{args[1]}') is False:
            print('** no instance found **')
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            name_id = f'{args[0]}.{args[1]}'
            all_instances = storage.all()
            instance = all_instances[name_id]
            attr_name = args[2]
            attr_value = args[3].strip('"')
            if not hasattr(instance, attr_name):
                if attr_value.isdigit():
                    setattr(instance, attr_name, int(attr_value))
                elif self.isfloat(attr_value):
                    setattr(instance, attr_name, float(attr_value))
                else:
                    setattr(instance, attr_name, str(attr_value))
            else:
                cav = type(getattr(instance, attr_name))(attr_value)
                setattr(instance, attr_name, cav)

            storage.save()

    def do_test(self, line):
        """ test method for experiments. """
        if self.find('BaseModel.d59ae699-629b-4dd9-be1c-e8449990e04c') is True:
            print("found it")
        else:
            print("not found")

    def default(self, line):
        """
        Method for custom commands.
        """
        args = line.split(' ')
        if len(args) == 1 and '.' in line:
            args2 = line.split('.')
            if args2[1] == 'all()':
                if args2[0] not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                else:
                    all_instances = storage.all()
                    insts = [
                            f"{v}" for v in all_instances.values()
                            if v.__class__.__name__ == args2[0]
                            ]
                    print(insts)
            elif args2[1] == 'count()':
                if args2[0] not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                else:
                    all_instances = storage.all()
                    insts = [
                            f"{v}" for v in all_instances.values()
                            if v.__class__.__name__ == args2[0]
                            ]
                    print(len(insts))
            elif 'show(' in args2[1]:
                if args2[0] not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                else:
                    args_show = line.split('(')
                    show_id = args_show[1].split(')')
                    class_name = args2[0]
                    instance_key = f'{class_name}.{show_id[0]}'
                    if self.find(instance_key) is False:
                        print("** no instance found **")
                    else:
                        all_instances = storage.all()
                        print(all_instances[instance_key])
            elif 'destroy(' in args2[1]:
                if args2[0] not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                else:
                    args_show = line.split('(')
                    show_id = args_show[1].split(')')
                    class_name = args2[0]
                    instance_key = f'{class_name}.{show_id[0]}'
                    if self.find(instance_key) is False:
                        print("** no instance found **")
                    else:
                        all_instances = storage.all()
                        del all_instances[instance_key]
                        storage.save()
            else:
                print(f"*** Unknown syntax: {line}")
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
