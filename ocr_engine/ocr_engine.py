#!/usr/bin/env python3
"""
This module handles the processing of images and interface with Tesseract
service;

Returns
-------
str
    returns a string representation of the predicted text in the image.
"""


from PIL import Image
import pytesseract
from pytesseract import Output

def ocr_engine(filename=str) -> str:
    """
    ocr_engine 

    This function will handle the engine OCR processing of images.

    Parameters
    ----------
    filename : str, optional
        string with the file name to be processed, by default str

    Returns
    -------
    str
        returns a string representation of the predicted text in the image.
    """

    text = pytesseract.image_to_string(Image.open(filename)) # Text in the image
    data = pytesseract.image_to_data(Image.open(filename), output_type=Output.DICT) # other parameters extracted from the image, like confidence, boxes, and so on
    
    def average_confidence_calc(data):
        """Calculates the average conficence level of the prediction"""

        sum_confidence = 0
        count = 0
        for i in data["conf"]:
            if isinstance(i, int):
                sum_confidence += i
                count += 1
        return round(sum_confidence / count,2)


    result = {"text": text, "average_confidence": average_confidence_calc(data), "confidence_list": data["conf"]}
    return result
