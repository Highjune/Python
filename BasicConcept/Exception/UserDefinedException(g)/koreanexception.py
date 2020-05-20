#koreanexception.py

#main8이랑
#사용자 정의 함수의 조건 2가지
#1.Exception의 자식
#2.부모에게 메시지 보내야됨 
class KoreanException(Exception): 
    """국어점수가 0부터 100점의 범위가 아닌 경우 유발시키는 Exception"""
    def __init__(self):
        # Exception.__init__(self, "국어점수는 0부터 100점 사이여야 합니다.")  #자식이 부모의 생성자에 접근하는 방법 중 1.exception객체로 접근할 때는 self
        super().__init__("국어점수는 0부터 100점 사이여야 합니다.") #2. super()로 접근하면 self없어도 된다.


    