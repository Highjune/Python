#child.py
from parent import Parent
class Child(Parent):
    def __init__(self, name, salary, gender):
        super().__init__(name, salary)
        self._gender = gender

    def __str__(self):
        print(super().__str__(), end = '')
        return ', 성별 = {}'.format(self._gender)
    
chulsu = Child('김철수', 3000, '남성')
print(chulsu)

print(issubclass(Child, Parent))
