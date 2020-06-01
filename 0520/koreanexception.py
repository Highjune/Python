#koreanexception.py
class KoreanException(Exception):
    """국어점수가 0부터 100점의 범위가 아닌 경우 유발시키는 Exceptioin"""
    def __init__(self):
        #Exception.__init__(self, "국어점수는 0부터 100점 사이여야 합니다.")
        super().__init__("국어점수는 0부터 100점 사이여야 합니다.")