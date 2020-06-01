from koreanexception import *

class Student:
    def __init__(self, name, kor):
        self._name = name
        if 0 <= kor <= 100 : 
            self._kor = kor
        else : 
            raise KoreanException()

    @property
    def kor(self): return self._kor
    @property
    def name(self): return self._name

try:
    jimin = Student('한지민', 199)
except KoreanException as e: 
    print(e.args[0])
except Exception as e:
    print(e.args)
else : 
    print(jimin.kor)