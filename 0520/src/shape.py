#shape.py
class Shape(object):
    def __init__(self, name):
        self._name = name
        
    def calcArea(self):
        raise NotImplementedError('필수...')