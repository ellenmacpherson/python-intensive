#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:36:03 2019

@author: ellenmacpherson
"""

import sqlite3

conn = sqlite3.connect('task1.db')
c = conn.cursor()

def create_table():
    