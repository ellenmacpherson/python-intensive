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

        
        
#
# Hence, a call r() returns a random value between 0 and 1, with which you introduce variation into the movement vectors. Try typing r() into your console to see what it does .
#As 10 has been a reasonable value for self.dx so far, you might now assign a value such as 5 + 10 * r(), which will be a random value between 5 and 15. Implement this idea for both the x and y velocity components. Run the test file several times to see the variations introduced .