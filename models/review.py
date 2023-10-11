#!/usr/bin/python3
""" teview class / model ."""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class / model . """
    place_id = ""
    user_id = ""
    text = ""
