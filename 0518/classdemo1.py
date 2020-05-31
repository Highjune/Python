class Employee : 
    """Employee 객체의 설계도입니다."""
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def toString(self):
        return 'name = {}'.format(self.name)

smith = Employee('스미스')
#print(help(smith))

# print(smith.getName())
# smith.setName('마이클')
# print(smith.toString())

smith.age = 27
# smith.age = 28
# print(smith.age)

if hasattr(smith, 'age') == True : 
    print(getattr(smith, 'age'))
    setattr(smith, 'age', 28)
    print(getattr(smith, 'age'))
    delattr(smith, 'age')

print(smith.age)
