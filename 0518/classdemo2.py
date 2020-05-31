class Product : 
    def __init__(self, name):
        self._name = name
    @property
    def name(self): return self._name     #getter

    @name.setter
    def name(self, name): self._name = name
    def __str__(self): return '이름 = ' + self._name

ballpen = Product('모나미볼펜')
print(ballpen.name)   #getter
ballpen.name = '샤프펜슬'   #setter
print(ballpen)   #toString 