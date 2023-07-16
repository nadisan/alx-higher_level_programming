#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys
import json
import pep8


class TestBase(unittest.TestCase):
    """clas base test"""
    def test_id(self):
        """check id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertIsNotNone(id(b1))

    def test_init(self):
        """ test for proper instance creation"""
        Base._Base__nb_objects = 0
        b2 = Base()
        self.assertIsInstance(b2, Base)

    def test_numobj(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_toJsonString(self):
        """check to_JsonString"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        t_dict = r1.to_dictionary()
        json_string = json.dumps([t_dict])
        json_listdict = r1.to_json_string([t_dict])
        self.assertTrue(json_string == json_listdict)

    def test_saveToFile(self):
        """check save_to_file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2)
        t_dict = [r1.to_dictionary(), r2.to_dictionary()]
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            list_dict = json.loads(f.read())
        self.assertTrue(t_dict == list_dict)

    def test_fromJsonString(self):
        """check from_json_string"""
        Base._Base__nb_objects = 0
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(list_input == list_output)

    def test_empty(self):
        """ check empty argument"""
        Base._Base_nb_objects = 0
        r1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = None
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = ""

    def test_pep8_model(self):
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
