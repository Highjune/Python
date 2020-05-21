#GradeCheckException.py

class GradeCheckError(Exception) :
    def __init__(self):
        super().__init__("등급은 1 ~ 5 등급까지만 유효합니다.")