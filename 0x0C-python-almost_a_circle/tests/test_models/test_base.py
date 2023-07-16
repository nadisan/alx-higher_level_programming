#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
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

    def test_create(self):
        """check load from file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dic = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dic)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_loadFromFile(self):
        """check save_to_file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(3, 2)
        list_rect_input = [r1, r2]
        Rectangle.save_to_file(list_rect_input)
        list_rect_output = Rectangle.load_from_file()
        self.assertTrue(type(list_rect_output) == list)
        for rec in list_rect_input:
            self.assertTrue(isinstance(rec, Rectangle))
        for rec in list_rect_output:
            self.assertTrue(isinstance(rec, Rectangle))
        s1 = Square(10)
        s2 = Square(3, 2, 10)
        list_sq_input = [s1, s2]
        Square.save_to_file(list_sq_input)
        list_sq_output = Square.load_from_file()
        self.assertTrue(type(list_sq_output) == list)
        for sq in list_sq_input:
            self.assertTrue(isinstance(sq, Square))
        for rec in list_rect_output:
            self.assertTrue(isinstance(sq, Square))

    def test_pep8_model(self):
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
