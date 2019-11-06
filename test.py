#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:45:59 2019

@author: rahul
"""

import pytesseract
from PIL import Image

filename = "/home/rahul/Downloads/damaso question set/D.I. (TQ-10) 5 OPTION/Option Wise-10/FIVE OPTIONS-10/E-1/Q-738/Q-7.jpg"

outfile = "exampletext.txt"

f = open(outfile, "a")

text = str(((pytesseract.image_to_string(Image.open(filename))))) 

f.write(text)

f.close()