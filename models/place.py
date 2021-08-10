#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer, String
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship, backref
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref=backref(
            "place", cascade="all, delete"))
    else:
        @property
        def reviews(self):
            """the geter of cities"""
            from models.review import Review
            objs = models.storage.all(Review)
            new_list = []
            for review in objs.values():
                if review.place_id == self.id:
                    new_list.append(review)
            return new_list
