#triangle.py
from shape import Shape

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self._base = base
        self._height = height
        self._area = None
        
    @property
    def area(self): return self._area
    
    def calcArea(self):
        self._area = (self._base * self._height) / 2
        
    def __str__(self):
        return self.__class__.__name__ + '의 면적은 '     
        
        
        
