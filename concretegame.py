'''concrete game'''

from gametemplate import GameTemplate

class ConcreteGame(GameTemplate):
    '''need documentation'''

    def __init__(self, name):
        '''need documentation'''
        super(ConcreteGame, self).__init__()
        self._name = name
        self._gameobjects = []


    def addtobatch(self, gameobject):
        '''add gameobjects to this game'''
        self._gameobjects.append(gameobject)

    def update(self):
        '''update this games logic'''
        if not super(ConcreteGame, self)._update():
            return False
        return True

    def draw(self):
        '''draw all gameobjects added to this game'''
        super(ConcreteGame, self)._draw()

    def run(self):
        '''need documentation'''
        if super(ConcreteGame, self)._startup():
            while self.update():
                self.draw()
        super(ConcreteGame, self)._shutdown()