#!/usr/bin/python3
''' Test suite for the console'''

import os
import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    """ Test the console module """

    def create(self):
        """ create instance of HBNBCommand class """
        return HBNBCommand()


   # @unittest.skipIf(
      #  os.getenv('HBNB_TYPE_STORAGE') == 'db',
      #  "won't work in db")
    #def test_show(self):
       # '''
         #   Testing that show exists
        #'''
       # console = self.create()
       # console.onecmd("create User")
       # user_id = self.capt_out.getvalue()
       # sys.stdout = self.backup
        #self.capt_out.close()
       # self.capt_out = StringIO()
       # sys.stdout = self.capt_out
       # console.onecmd("show User " + user_id)
       # x = (self.capt_out.getvalue())
       # sys.stdout = self.backup
       # self.assertTrue(isinstance(x, str))
