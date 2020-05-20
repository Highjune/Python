#myclass.py
class Shape : 
    def __init__(self, x = 0, y = 0):
        self._x = x; self._y = y
        
    def move(self, x, y):
        return Shape(self._x + x, self._y + y)
    
    def __str__(self):
        return '(x, y) = ({}, {})'.format(self._x, self._y)
    
    @staticmethod
    def getname():
        return __class__.__name__

class Triangle : 
    count = 0   #class variable
    
    @classmethod
    def getCount(cls):
        return cls.count
    
    def __init__(self, base, height, x = 0, y = 0):
        self._base = base
        self._height = height
        self._x = x
        self._y = y
        Triangle.count = Triangle.count + 1
    
    def calcArea(self):
        return (self._base * self._height) / 2
    
    def __str__(self):
        return '(밑변, 높이, x, y) = ({},{},{},{})'.format(self._base,
                        self._height, self._x, self._y) 
    
    
    
    
    
    
    
    
    
    