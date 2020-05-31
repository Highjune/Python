class Car :
    count = 0    #class variable
    def __init__(self, name, price, maker):   #생성자
        self.name = name
        self.price = price
        self.maker = maker
        Car.count += 1 

    def toString(self):   #member method
        return 'name = %s, price = %d, maker = %s' % (self.name, self.price, self.maker)

    @classmethod
    def getCount(cls):
        return cls.count

    @staticmethod
    def myprint():
        print('Hello, World')

sonata = Car('소나타', 25000000, 'Hyundai')
matiz = Car('마티즈', 10000000, 'Daewoo')
carnival = Car('카니발', 35000000, 'KIA')
#print(carnival.getCount())
print(Car.getCount())
Car.myprint()