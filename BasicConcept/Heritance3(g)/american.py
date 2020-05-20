#american.py
import mammal

class American(mammal.Mammal):
    def __init__(self, name):
        self._name = name
        
    def saySomething(self):
        print(self._name + '이(가) Good Morning')