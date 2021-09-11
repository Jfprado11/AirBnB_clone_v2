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
            # from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
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
            if "id" not in self.__dict__:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        new_dict = self.__dict__.copy()
        del new_dict["_sa_instance_state"]
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, new_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at':
                new_dict[key] = self.created_at.isoformat()
            elif key == 'updated_at':
                new_dict[key] = self.updated_at.isoformat()
            elif key == '_sa_instance_state':
                continue
            else:
                new_dict[key] = value

        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def delete(self):
        """delete the object instance"""
        from models import storage
        storage.delete(self)
