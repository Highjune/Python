class Employee:
    """Employee 객체의 설계도입니다."""
    def __init__(self, name): #생성자
        self.name = name

    def getName(self): #getter
        return self.name

    def setName(self, newName): #setter
        self.name = newName

    def toString(self): #toString
        return 'name = {}'.format(self.name)

smith = Employee('스미스')
# print(help(smith))

# print(smith.getName())
# smith.setName('마이클')
# print(smith.toString())

smith.age = 27 #설계도(class)에 없어도 새로 만들 수 있다.
smith.age = 28
print(smith.age)

if hasattr(smith, 'age') == True :
    print(getattr(smith, 'age'))
    setattr(smith, 'age', 28)
    print(getattr(smith, 'age'))
    delattr(smith, 'age')

print(smith.age)

