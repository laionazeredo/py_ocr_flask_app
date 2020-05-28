#!/usr/bin/env python3
"""
This module handles the processing of images and interface with Tesseract service;

Returns
-------
str
    returns a string representation of the predicted text in the image.
"""

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_engine(filename=str) -> str:
    """This function will handle the engine OCR processing of images."""
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_engine('images/ocr_example_1.png'))