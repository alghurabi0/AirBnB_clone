#!/usr/bin/python3
""" test cases for the console. """
import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ test cases for the console. """
    @classmethod
    def setUpClass(cls):
        """ set up class. """
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """ tear down class. """
        cls.console = None

    def tearDown(self):
        """ tead down. """
        self.console.postloop()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create_command(self):
        """ test create command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(output != "" and len(output) == 36)

    def test_show_command(self):
        """ test show command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            uid = f.getvalue().strip()
            self.console.onecmd(f"show User {uid}")
            output = f.getvalue().strip()
            self.assertTrue(f"[User] ({uid}) " in output)

    def test_destroy_command(self):
        """ test destroy command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            uid = f.getvalue().strip()
            self.console.onecmd(f"destroy User {uid}")
            self.console.onecmd(f"show User {uid}")
            output = f.getvalue().strip()
            self.assertTrue("no instance found" in output)

    def test_all_command(self):
        """ test all command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue("User" in output)

    def test_update_command(self):
        """ test update command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            uid = f.getvalue().strip()
            self.console.onecmd(f"update User {uid} first_name 'John'")
            self.console.onecmd(f"show User {uid}")
            output = f.getvalue().strip()
            self.assertTrue("John" in output)


if __name__ == '__main__':
    unittest.main()
