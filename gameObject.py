import pygame

class GameObject(object):
    def __init__(self, spot):
        self._surface = pygame.Surface((15, 15))
        self._surface.fill((125, 125, 125))
        self._position = spot
        self._lifetime = 0

        
    def update(self, dt):
        self._lifetime += dt
        

    def draw(self, surface):
        surface.blit(self._surface, self._position)