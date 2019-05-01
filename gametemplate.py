'''gametemplate.py'''

#from gameobject import GameObject
import pygame
from Engine.constants import *

class GameTemplate(object):
    '''pygame object'''
    def __init__(self):
        '''abc'''
        pygame.init()

    def _startup(self):
        return True

    def _update(self):
        '''input and time'''
        return True

    def _draw(self):
        '''base draw'''

    def _shutdown(self):
        '''shutdown the game properly'''