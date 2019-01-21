#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:23:27 2019

@author: ellenmacpherson
"""
import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('mock_data_table.db')
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
#    c.close()
#    conn.close() #Need to close the table and database with these two commands.

create_table()
data_entry()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d  %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)', (unix,date, keyword, value))
    conn.commit()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1) #Slows down the process - computers work so fast at inputting data we would have a lot of similar values. There would be no need for this in a real-world insertion

#Pulling all values from task2.db where value = 8.
def read_from_db_all():
    c.execute('SELECT * FROM stuffToBuild WHERE value = 8')
    for row in c.fetchall(): #Similar to pull function in git. After nominating which column to select, you need to use this function to produce the action.
        print(row)

def read_from_db2():
    c.execute('SELECT * FROM stuffToBuild WHERE value = 8 and unix > 1534855733 and unix < 1534855741') #Currently not returning any data
    for row in c.fetchall():
        print(row[0])

#Storing data gathered in a list of tuples
def create_list():
    db_list = []
    c.execute('SELECT * FROM stuffToBuild WHERE value > 5 and value < 8')
    for row in c.fetchall():
        db_list.append(row)
    print (db_list)
    return db_list

#Storing specific unix data ordered in ascending values
def unix_list():
    unix_list = []
    c.execute('SELECT unix FROM stuffToBuild WHERE value > 3 and value < 5 ORDER BY unix')
    for row in c.fetchall():
        unix_list.append(row)
    print (unix_list)
    return unix_list


#read_from_db_all()
#read_from_db2()
#create_list()
unix_list()

c.close()
conn.close()
