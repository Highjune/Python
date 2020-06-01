#student.py
import person
class Student(person.Person):
    def __init__(self, name, age, hakbun):
        super().__init__(name, age)
        self._hakbun = hakbun
        
    def __str__(self):
        return '이름 = {}, 나이 = {}, 학번 = {}'.format(self._name, self._age, self._hakbun)
    
    