#square.py
from shape import Shape

class Square(Shape): #shape을 상속
    def __init__(self, name, width, height):
        super().__init__(name)
        self._width = width
        self._height = height
        self._area = None
        
    @property        
    def area(self): return self._area
        
    def calcArea(self): #부모것 재정의
        self._area = self._width * self._height
        
    def __str__(self):
        return self.__class__.__name__ + '의 면적은 '