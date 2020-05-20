from koreanexception import *
class Student:
    def __init__(self, name, kor):
        self._name = name
        if 0 <= kor <= 100 :
            self._kor = kor
        else :
            raise KoreanException

    @property
    def kor(self):return self._kor
    @property
    def name(self):return self._name


try :
    jimin = Student('한지민', 99)
except KoreanException as e:
    print(e.args[0]) #tuple이기 때문에 0으로 뽑음
except Exception as e :
    print(e.args)
else :
    print(jimin.kor)
