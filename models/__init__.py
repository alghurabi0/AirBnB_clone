#!/usr/bin/python3
""" Initialization of the project. """

from models.engine import file_storage

storage = file_storage.FileStorage()

storage.reload()
