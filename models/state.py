#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship

from os import getenv


class State(BaseModel, Base):
    """ State class """
    # if getenv("HBNB_TYPE_STORAGE") == "db":
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
    # else:
    if getenv("HBNB_TYPE_STORAGE") != "db":
        name = ""

        @property
        def cities(self):
            my_list = []
            my_dict = models.storage.all('City')
            for city, value in my_dict.items():
                if self.id == city.state_id:
                    my_list.append(value)
            return my_list
