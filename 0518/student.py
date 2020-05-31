#student.py
class Student:
    def __init__(self, name, age, city, gender):  #Constructor
        self._name = name; self._age = age; self._city = city;  self._gender = gender
    @property
    def name(self): return self._name
    @name.setter
    def name(self, name): self._name = name

    @property
    def age(self):  return self._age
    @age.setter
    def age(self, age): self._age = age

    @property
    def city(self): return self._city
    @city.setter
    def city(self, city): self._city = city

    @property
    def gender(self):  return self._gender
    @gender.setter
    def gender(self, gender):  self._gender = gender

    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self._name, self._age, self._city, self._gender)
