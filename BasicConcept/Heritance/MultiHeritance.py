class Mammal:
    def __init__(self):
        self._name = "Dog"

class Birds :
    def __init__(self):
        self._name = "Sparrow"
    
    
class Bat(Birds, Mammal): #둘을 상속했지만 Mammal가 우선순위를 갖는다.(먼저 상속받은 것 먼저)
    @property
    def name(self): return self._name

bat = Bat()
print(bat.name) #먼저 상속받은 것 나옴
print(Mammal()._name)
print(Birds()._name)
bat._name = 'Cat' #bat는 _name을 갖고 있지 않지만 부모것을 사용가능
print(bat.name)

# print(dir(bat)) #dir을 사용하면 그 안의 멤버를 다 확인할 수 있다.
# print(bat.__class.__.__name__)
# print(dir(Mammal)) 
