#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:37:19 2019

@author: ellenmacpherson
"""
import sqlite3

conn = sqlite3.connect('business_phonebook.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS business_phonebook(name TEXT, category TEXT, building_no INT, street_name TEXT, postcode TEXT, telephone INT, x_coord FLOAT, y_coord FLOAT)')
    c.execute('CREATE TABLE IF NOT EXISTS person_phonebook(name TEXT, building_no INT, street_name TEXT, postcode TEXT, telephone INT, x_coord FLOAT, y_coord FLOAT)')
    
create_table()