import pygame
import math
import time
from Vec2D import vec
import random

class Vec2D(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x, self.y + other.y)

    def __str__(self):
        return 'someething' % (self.x, self.y)    

    def getdata(self):
        return (self.x, self.y)

    def length(self):
        return math.sqrt(self.square_length())

    def normalize(self):
        length = self.length()
        if length == 0.0:
            return Vec2D(0, 0)
        return Vec2D(self.x/length, self.y/length)

def flee(self, getTime):
    self.Number = getTime()

if now = nextDecision 


def wander(self):
    self.               


