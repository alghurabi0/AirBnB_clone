#!/usr/bin/python3
""" Console module for devs. """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command line cmd. """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ quits the command line. """
        exit()

    def do_EOF(self, line):
        """ Signals EOF to cmd. """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
