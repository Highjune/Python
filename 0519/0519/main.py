class Car:
    name = None
    def __init__(self):   #생성자
        print('방금 객체가 생성됐습니다.')

    def __del__(self):    #소멸자
        print('방금 객체가 소멸됐습니다.')

car = Car()
#1.
car = None

#2. 
car1 = Car()

#3. 
del car1