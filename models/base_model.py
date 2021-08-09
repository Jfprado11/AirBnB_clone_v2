#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from re import S
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, String


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # Not sure if it works
        if '_sa_instance_state' in dictionary:
            dictionary.pop('_sa_instance_state')
        return dictionary

    def delete(self):
        """delete the object instance"""
        from models import storage
        storage.delete(self)
