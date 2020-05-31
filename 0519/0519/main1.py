class Car : 
    '''자동차에 대한 prototype 객체'''
    def print_info(self):
        class_name = self.__class__.__name__
        print('My name is ' + class_name)

sonata = Car()
print(Car.__doc__)
print(Car.__bases__)
#print(Car.__name__)
sonata.print_info()