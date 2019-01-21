#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:52:01 2019

@author: ellenmacpherson
"""

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('mock_data_table.db')
c = conn.cursor()

import json
import requests
from pprint import pprint

with open('mock_data_business_json.json') as f:
    data = json.load(f)
    
print (data[0])

all_data = []

def get_row_info():
    for i in data:
        all_data.append(i)
    return all_data

query = "INSERT INTO mock_data_table(business_name) VALUES"

bus_name = []
address_1 = []
address_2 = []
address_3 = []
postcode = []
country = []
tel_no = []
bus_cat = []

def get_info():
    for i in data:
        bus_name.append(i["business name"])
        postcode.append(i["postcode"])
        address_1.append(i["address_line_1"])
        address_2.append(i["address_line_2"])
        address_3.append(i["address_line_3"])
        country.append(i["country"])
        tel_no.append(i["telephone_number"])
        bus_cat.append(i["business_category"])

get_info()
get_row_info()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS mock_data_table(business_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode TEXT, country TEXT, telephone_number TEXT, business_category TEXT)') 

def data_entry():
    for i in bus_name: 
        c.execute(query, [i])
    
data_entry()
#data_entry()
     
c.close()
conn.close()





    
    