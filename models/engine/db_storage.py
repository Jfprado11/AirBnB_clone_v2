#!/usr/bin/python3
"""module contais the class dbsotrage
for the creation of the engine with ORM
"""
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from os import getenv

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """class for the engine with sql"""

    __engine = None
    __session = None

    def __init__(self):
        """the constructor for creating the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'), getenv(
                'HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        cls_dict = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                key_obj = cls.__name__ + '.' + obj.id
                cls_dict[key_obj] = obj
        else:
            cls_list = [User, State, City, Amenity, Place, Review]
            for cls_type in cls_list:
                for obj in self.__session.query(cls_type):
                    key_obj = cls_type.__name__ + '.' + obj.id
                    cls_dict[key_obj] = obj
        return cls_dict

    def new(self, obj):
        """add the object to the current database"""
        # Session = sessionmaker(bind=self.__engine)
        # self.__session = Session()
        self.__session.add(obj)
        # self.__session.close()

    def save(self):
        """save teh curent session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current seesion"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all the databale and create the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """removing the session"""
        self.__session.remove()
