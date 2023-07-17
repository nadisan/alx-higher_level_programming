#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys
import json
import pep8


class TestRectangle(unittest.TestCase):
    """clas rectangle test"""
    def test_id(self):
        """check id"""
        Base._Base_nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertIsNotNone(id(r1))

    def test_init(self):
        """ test for proper instance creation"""
        Base._Base_nb_objects = 0
        r2 = Rectangle(2, 10)
        self.assertIsInstance(r2, Rectangle)

    def test_numObj(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(10, 2, 0, 0)
        r4 = Rectangle(5, 5)
        self.assertEqual(r4.id, 2)

    def test_getterAndSetter(self):
        """checks getter and setter"""
        Base._Base__nb_objects = 0
        r5 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)

    def test_area(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        r6 = Rectangle(10, 2)
        self.assertEqual(r6.area(), r6.width * r6.height)

    def test_display(self):
        """check display"""
        Base._Base__nb_objects = 0
        r7 = Rectangle(4, 3)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r7.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string,
                         "####\n####\n####\n")

    def test_str(self):
        """check str"""
        Base._Base__nb_objects = 0
        r8 = Rectangle(10, 6, 2, 1, 12)
        r9 = Rectangle(5, 5, 1)
        string1 = r8.__str__()
        string2 = r9.__str__()
        self.assertEqual(string1,
                         "[Rectangle] (12) 2/1 - 10/6")
        self.assertEqual(string2,
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_display_xy(self):
        """check display xy"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3, 2, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r1.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string,
                         "\n\n  ##\n  ##\n  ##\n")

    def test_update_kwargs(self):
        """checks update kwargs"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (1) 10/10 - 10/10")
        r1.update(x=1, height=2, y=3, width=4, id=89)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 1/3 - 4/2")
    
    def test_empty(self):
        """ check empty argument"""
        Base._Base_nb_objects = 0
        r1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = None
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = ""

    def test_pep8_model(self):
        """check dictionary"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """ check dictionary"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
