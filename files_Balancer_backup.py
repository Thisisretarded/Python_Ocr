#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:33:54 2019

Read the names of .jpg files in the directory and create a sep file for each
number present in the file

@author: rahul
"""

mode = "Development"

#Importing Libraries
import os
import pandas as pd
from pathlib import Path
import logging

def logger(msg, path, level):
    """ function responsible for logging
    """
    if level == "DEBUG":
        logging.debug(msg+" --> "+str(path))
    elif level == "INFO":
        logging.info(msg+" --> "+str(path))


def recursefunct(inputdir):
    
    content = os.listdir(inputdir)
    for dirctry in content:
        if not ".jpg" in dirctry:
            logger("cant found jpg file here", os.path.join(inputdir, dirctry), "INFO")
            var = inputdir
            inputdir=os.path.join(inputdir, dirctry)
            if os.path.isdir(inputdir):
                recursefunct(os.path.join(var, dirctry))
            elif os.path.isfile(inputdir):
                logger("found a file at: ", inputdir, "INFO")
                return
            else:
                logger("Wrong address !! continued at ", inputdir, "INFO")
                continue
        else:
            logger("Found JPG's here mark this address!!!", inputdir, "INFO")

if __name__ == "__main__":
    
    if mode == "Development":
        x = "log.txt"
        inputdir = "/home/rahul/anaconda3/bin/Edu.Data (Complete & Option-Wise )(TQ-46301)/SSC (TQ-35884)4,5 OPTION/REASONING (TQ-8832), 4-5 OPTIONS/Option Wise-8832"
    elif mode == "Deploy":
        x = input("Please Input ame of log file:   ")
        inputdir = input("Enter the directiory path:    ")
        
    logging.basicConfig(level=20, filename = x)
    
    recursefunct(inputdir)