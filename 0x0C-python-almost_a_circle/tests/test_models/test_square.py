#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys
import json
import pep8


class TestSquare(unittest.TestCase):
    """clas square test"""
    def test_id(self):
        """check id"""
        Base._Base_nb_objects = 0
        s1 = Square(10)
        self.assertIsNotNone(id(s1))

    def test_init(self):
        """ test for proper instance creation"""
        Base._Base_nb_objects = 0
        s2 = Square(6)
        self.assertIsInstance(s2, Square)

    def test_numObj(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        s3 = Square(2, 2)
        s4 = Square(5, 5)
        self.assertEqual(s4.id, 2)

    def test_getterAndSetter(self):
        """checks getter and setter"""
        Base._Base__nb_objects = 0
        s5 = Square(5)
        self.assertEqual(s5.width, 5)
        self.assertEqual(s5.height, 5)
        s5 = Square(2, 2)
        self.assertEqual(s5.width, 2)
        self.assertEqual(s5.height, 2)
        self.assertEqual(s5.x, 2)
        s5 = Square(3, 1, 3)
        self.assertEqual(s5.width, 3)
        self.assertEqual(s5.height, 3)
        self.assertEqual(s5.x, 1)
        self.assertEqual(s5.y, 3)

    def test_area(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        s6 = Square(5)
        self.assertEqual(s6.area(), s6.width * s6.height)

    def test_display(self):
        """check display"""
        Base._Base__nb_objects = 0
        s7 = Square(5)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s7.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string,
                         "#####\n#####\n#####\n#####\n#####\n")

    def test_str(self):
        """check str"""
        Base._Base__nb_objects = 0
        s8 = Square(5)
        s9 = Square(2, 2)
        s10 = Square(3, 1, 3)
        string1 = s8.__str__()
        string2 = s9.__str__()
        string3 = s10.__str__()
        self.assertEqual(string1, "[Square] ({:d}) 0/0 - 5".format(s8.id))
        self.assertEqual(string2, "[Square] ({:d}) 2/0 - 2".format(s9.id))
        self.assertEqual(string3, "[Square] ({:d}) 1/3 - 3".format(s10.id))

    def test_display_xy(self):
        """check display xy"""
        Base._Base__nb_objects = 0
        s1 = Square(2, 3, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s1.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string,
                         "\n\n   ##\n   ##\n")
        s2 = Square(3, 2, 1)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s2.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n  ###\n  ###\n  ###\n")

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

    def test_dictionary(self):
        """ check dictionary"""
        Base._Base_nb_objects = 0
        s1 = Square(10, 2, 1, 1)
        s1_dictionary = s1.to_dictionary()
        a_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertTrue(s1_dictionary == a_dict)

    def test_pep8_model(self):
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
