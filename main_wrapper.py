#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:31:17 2019

@author: rahul
"""

# import libraries

import os
import pandas as pd
import pytesseract
from PIL import Image


def tesseract_funct(filename):
    return str(((pytesseract.image_to_string(Image.open(filename)))))

#Iterte over directories
input("Input the parent path")