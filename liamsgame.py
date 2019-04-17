'''concrete game'''
# pylint: disable=E1121
from game import Game
import pygame
from constants import *

class LiamsGame(Game):
    '''need documentation'''

    def __init__(self, name):
        '''need documentation'''
        super(LiamsGame, self).__init__()
        self._name = name
        self._gameobjects = []

        self._font = pygame.font.Font(None, 24)
        self.pause_surface = pygame.Surface(
            (self._screen.get_size()[0] / 3, self._screen.get_size()[1] / 3))
        self.pause_surface.fill(GREEN)
        self.pause_rect = self.pause_surface.get_rect()

    def addtobatch(self, gameobject):
        '''need documentation'''
        self._gameobjects.append(gameobject)

    def update(self):
        '''need documentation'''
        if not super(LiamsGame, self)._update():
            return False
        for event in self._events:
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.constants.K_e]:
                    self.gamestate = "pause"
                if keystate[pygame.constants.K_r]:
                    self.gamestate = "quit"

        for gameobject in self._gameobjects:
            gameobject.update(self._clock.get_time())

        return True

    def draw(self):
        '''need documentation'''
        self._screen.blit(self._background, (0, 0))
        for gameobject in self._gameobjects:
            gameobject.draw(self._screen)

        if self.gamestate == "pause":

            self.pause_surface.blit(self._font.render(
                "PAUSED", True, WHITE), self.pause_rect.move(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3))

            self._screen.blit(self._background, (0, 0))
            self._screen.blit(self.pause_surface, (0, 0))

        pygame.display.flip()

    def run(self):
        '''need documentation'''
        if super(LiamsGame, self)._startup():
            while self.update():
                self.draw()
        super(LiamsGame, self)._shutdown()