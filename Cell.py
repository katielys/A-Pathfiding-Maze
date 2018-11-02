class Cell():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.f = 0
        self.g = 0
        self.h = 0
     #funcao que compara se uma posicao eh igual a outra
    def __eq__(self, other):
        return self.position == other.position