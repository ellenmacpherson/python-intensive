#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:08:36 2019

@author: ellenmacpherson
"""
import sqlite3

conn = sqlite3.connect('task1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)') 
    #SQL commands are in uppercase - they don't have to be, but it helps to distinguish which are SQL related commands and which are table and column names for the that you give for the database.
    #stuffToBuild is the database table name
    #unix, datestamp, keyword and value are the column names
    #REAL and TEXT are the data types/format in each column - SQL language

def data_entry(): 
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
    conn.commit() #This is similar to a git command - after pushing values to the database you need to run the commit command.
    c.close()
    conn.close() #Need to close the table and database with these two commands.
    
create_table()
data_entry()
    