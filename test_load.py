# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 23:05:33 2018

@author: Siyang
"""
import json
from RiotAPI import RiotAPI

    
    

file_directory = "matches1.json"
with open(file_directory, 'r') as json_data:
    data = json.loads(json_data)
    print(data)
