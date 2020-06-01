#dog.py
from mammal import Mammal

class Dog(Mammal):
    def __init__(self, name):
        self._name = name
        
    def saySomething(self):
        print(self._name + '이(가) 멍멍멍멍')