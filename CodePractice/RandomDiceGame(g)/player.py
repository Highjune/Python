import random

class Player : 
    """Game을 하는 선수"""
    
    def __init__(self, nickname):
        self._nickname = nickname
        
    def guess(self):
        self._myrandom = random.randint(1, 11);
        
    def __str__(self):
        return '축하합니다. {}님!!!'.format(self._nickname)
    
    @property
    def myrandom(self): return self._myrandom