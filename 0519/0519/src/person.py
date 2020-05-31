#person.py
from builtins import staticmethod
class Person:
    def __init__(self, name = 'unknown', age = 20):
        self._name = name;   self._age = age
        
    def __str__(self):
        return '이름 = ' + self._name + ', 나이 = ' + str(self._age)
    
    def __len__(self):
        return len([self._name, self._age])
    
    def __add__(self, other):
        return self._age + other._age
    
    def __eq__(self, other):
        return self._name == other._name and self._age == other._age
    
    def __rmul__(self, other):
        return self._age * other
    
