#circle.py
from shape import Shape
import math

class Circle(Shape):
    def __init__(self, name, r):
        super().__init__(name)
        self._r = r
        self._area = None
        
    @property
    def area(self): return self._area
    
    def calcArea(self):
        self._area = self._r ** 2 * math.pi
        
    def __str__(self):
        return self.__class__.__name__ + '의 면적은 '     
        
        
        
