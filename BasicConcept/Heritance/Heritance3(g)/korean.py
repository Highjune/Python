#korean.py
import mammal

class Korean(mammal.Mammal):
    def __init__(self, name):
        self._name = name
        
    def saySomething(self):
        print(self._name + '이(가) 안녕하세요.')