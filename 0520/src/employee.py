#employee.py
import person
class Employee(person.Person):
    def __init__(self, name, age, empno, salary):
        super().__init__(name, age)
        self._empno = empno
        self._salary = salary
        
    def __str__(self):
        return '이름 = {}, 나이 = {}, 사원번호= {}, 봉급  {}' \
            .format(self._name, self._age, self._empno, self._salary)