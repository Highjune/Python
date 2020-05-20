class Product :
    def __init__(self, name):
        self.name = name

    @property
    def Name(self) : return self.name #getter

    @name.setter
    def name(self, name) : self.name = Name #setter
    def __str__(self) : return '이름 = ' + self._name

ballpen = Product('모나미볼펜')
print(ballpen.name) #getter
ballpen.name = '샤프펜슬' #setter
print(ballpen.name)


