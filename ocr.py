#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:45:59 2019

@author: rahul
"""

import pytesseract
from PIL import Image

filename = input("Please enter the name of .jpg/Image file: ")

outfile = input("Please entar name of output file: ")

f = open(outfile, "a")

text = str(((pytesseract.image_to_string(Image.open(filename))))) 

f.write(text)

f.close()