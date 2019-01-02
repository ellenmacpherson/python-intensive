#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:33:32 2018

@author: ellenmacpherson
"""

from MovingShapes import * 

frame = Frame()
shape1 = Square(frame, 100)
for i in range(100):
    shape1.moveTick()