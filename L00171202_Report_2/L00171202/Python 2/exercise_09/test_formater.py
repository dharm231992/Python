"""
 Script: test_formater.py
 By: Dharmender Singh (L00171202)
 Tested: Python v3.10.8; Windows 11
 Date: 2nd November, 2022
"""

import unittest, formater

class TestFormater(unittest.TestCase):
    def test_lower(self):
        test_text = "DHARMENDER"
        result = formater.convert_lower(test_text)
        self.assertEqual(result, "dharmender")
    
    def test_upper(self):
        test_text = "Dharmender"
        result = formater.convert_upper(test_text)
        self.assertEqual(result, "DHARMENDER")

if __name__ =="__main":
    unittest.main()