#!/usr/bin/env python3

from app import Bmi
import unittest

class TestFunctions(unittest.TestCase):
    def test_basic(self):
        testcase = Bmi(50, 167)
        expected = {
        "bmi": 17.93,
        "label": "underweight"
        }
        self.assertEqual(testcase, expected)


if __name__ == '__main__':
      unittest.main()

