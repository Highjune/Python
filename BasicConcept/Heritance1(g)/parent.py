#parent.py
class Parent(object):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        
    def __str__(self):
        return '이름 = {}, 월급 = {}'.format(self._name, self._salary)