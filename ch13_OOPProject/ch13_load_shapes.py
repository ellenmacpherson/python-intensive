#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:26:51 2018

@author: ellenmacpherson
"""

from Shapes import *

frame = Frame()
s1 = Shape('square', 100)
s1.goto(200, 100) #Sends x to 200, 100 point on graph. Jump transition.

x = 0
y = 0

for i in range(100): #makes transition smoother. Loops x and y 100 times. 
    x = x + 5
    y = y + 5 
    s1.goto(x, y)
    
