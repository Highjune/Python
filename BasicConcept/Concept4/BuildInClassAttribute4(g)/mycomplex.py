import math

class MyComplex:

    def __init__(self, real, img):
        self._real = real
        self._img = img
        
    def __len__(self):
        return int(math.sqrt(self._real ** 2 + self._img ** 2))
    
    def __str__(self):
        if self._img > 0 : 
            return '{} + {}j'.format(self._real, self._img)
        else : return '{} - {}j'.format(self._real, self._img * -1) 
    
    def __add__(self, other):
        return MyComplex(self._real + other._real, self._img + other._img)
    
    def __sub__(self, other):
        return MyComplex(self._real - other._real, self._img - other._img)
    
    def __mul__(self, other):
        if type(other) == float:
            return MyComplex(self._real * other, self._img * other)
        elif type(other) == MyComplex : 
            return MyComplex(self._real * other._real - self._img * other._img,   
                             self._real * other._img + self._img * other._real)
    
    def __eq__(self, other):
        return self._real == other._real and self._img == other._img
    
    def __ne__(self, other):
        return self._real != other._real or self._img != other._img
    
        