class Student:
    def __init__(self, kor):
        if 0 <= kor <= 100 : 
            self._kor = kor
        else  : 
            raise  ValueError("국어점수는 0부터 100점사이입니다.")
    
    @property
    def kor(self): return self._kor

try:
    chulsu = Student(100)
except ValueError : 
    print("Error 발생")
else : print(chulsu.kor)