#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:12:04 2018

@author: ellenmacpherson
"""

from MovingShapes import *
frame = Frame()
numshapes = 3
shapes = []

for i in range(numshapes):
    shapes.append(Square(frame, 70)) #Setting values for square
    shapes.append(Diamond(frame, 70)) #Setting values for diamond
    shapes.append(Circle(frame, 70)) #Setting values for circle

for i in range(100):
    for shape in shapes:
        shape.moveTick()

frame.close()
