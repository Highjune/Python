#mammal.py
class Mammal(object):
    def __init__(self):
        raise NotImplementedError("반드시 자식 클래스를 필요로 합니다.")
    
    def saySomething(self):
        raise NotImplementedError("반드시 재정의 하십시오.")