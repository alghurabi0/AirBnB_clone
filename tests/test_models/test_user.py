#!/usr/bin/python3
""" test cases for user class. """
import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """ test cases for the user class. """
    def test_create_user(self):
        """ test create user. """
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_save_and_reload_user(self):
        """ test save and reload user . """
        user = User()
        user.email = "test@example.com"
        user.save()
        user_id = user.id
        req = f"User.{user_id}"
        storage.reload()
        reloaded_user = storage.all()[req]
        self.assertIsInstance(reloaded_user, User)
        self.assertEqual(reloaded_user.email, "test@example.com")

    def test_update_user_attributes(self):
        """ Test updating user attributes """
        user = User()
        user_id = user.id
        user.email = "test@example.com"
        user.save()

        user.email = "new@example.com"
        user.save()

        req = f"User.{user_id}"
        storage.reload()
        reloaded_user = storage.all()[req]
        self.assertEqual(reloaded_user.email, "new@example.com")

    def test_serialization_and_deserialization(self):
        """ Test serialization and deserialization of a user """
        user = User()
        user.email = "test@example.com"
        user_dict = user.to_dict()
        new_user = User(**user_dict)
        self.assertEqual(user.email, new_user.email)

    def test_all_users(self):
        """ Test retrieving all user objects """
        user1 = User()
        user1.email = "user1@example.com"
        user1.save()
        user2 = User()
        user2.email = "user2@example.com"
        user2.save()
        users = storage.all()
        inst = [user for user in users.values() if isinstance(user, User)]
        self.assertIn(user1, inst)
        self.assertIn(user2, inst)

if __name__ == '__main__':
    unittest.main()
