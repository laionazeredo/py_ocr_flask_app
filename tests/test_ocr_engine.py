# -*- coding: utf-8 -*-
import unittest

from ocr_engine import ocr_engine as ocre


class TestOCREngine(unittest.TestCase):
    def test_if_it_can_read(self):
        """Tests if the interface with Tesseract returns the correct value"""
        # Test cases
        self.file_short = 'tests/images/ocr_example_1_short.png'
        self.file_long = 'tests/images/ocr_example_2_long.jpg'
        
        # Call the function
        self.result_short = ocre.ocr_engine(self.file_short) #JENNIFER
        self.result_long = ocre.ocr_engine(self.file_long) #JENNIFER
        
        # Tests if it reads the asset properly
        self.assertEqual(self.result_short["text"], "JENNIFER") # Test case 1 -> expected True
        self.assertEqual(self.result_long["text"][0:10], "In 1929 Gu")

if __name__ == '__main__':
    unittest.main()
