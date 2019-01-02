##!/usr/bin/env python3
## -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:36:40 2018

@author: ellenmacpherson
"""
################################################################################
################################# IMPORTS ######################################
################################################################################

from Shapes import *
from pylab import random as r

################################################################################
############################## MOVING SHAPES ###################################
################################################################################

class MovingShapes():
    def __init__(self, frame, shape, diameter):
        self.frame = frame
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        
        #Defining minimum x and y values to later ensure the shapes bounce off the frame.
        self.minx = self.diameter / 2
        self.miny = self.diameter / 2
        self.maxx = frame.width - (self.diameter / 2)
        self.maxy = frame.height - (self.diameter / 2)
        
        #Assigning random start positions and random direction of movement to velocity.
        self.x = self.minx + (r() * (self.maxx - self.minx))
        self.y = self.miny + (r() * (self.maxy - self.miny))
        self.dx = 5 + 10 * r() #velocity
        self.dy = 5 + 10 * r() #velocity
        
    def goto(self, x, y):
        self.figure.goto(x, y)

    def moveTick(self):
        self.x += self.dx
        self.y += self.dy
        self.goto(self.x, self.y)
        
#If the shape hits the frame, move it away to a negative position on the relevant axis by multiplying the velocity value by -1.
        if self.x >= self.maxx:
            self.dx = (self.dx * -1)
        if self.y >= self.maxy:
            self.dy = (self.dy * -1)
        if self.x <= self.minx:
            self.dx = (self.dx * -1)
        if self.y <= self.miny:
            self.dy = (self.dy * -1)
        

class Square(MovingShapes):
    def __init__(self, frame, diameter):
        MovingShapes.__init__(self, frame, 'square', diameter) 

class Diamond(MovingShapes):
    def __init__(self, frame, diameter):
        MovingShapes.__init__(self, frame, 'diamond', diameter)
        #Overriding MovingShapes class values for diamond to avoid its shape overlapping hte border.
        self.maxx = frame.width - self.diameter
        self.maxy = frame.height - self.diameter
        self.minx = self.diameter
        self.miny = self.diameter

class Circle(MovingShapes):
    def __init__(self, frame, diameter):
        MovingShapes.__init__(self, frame, 'circle', diameter)
        

