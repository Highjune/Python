#person.py
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def workhard(self):
        print('부모의 메소드')