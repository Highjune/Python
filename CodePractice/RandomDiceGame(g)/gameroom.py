from player import Player
import random
#gameroom.py
class GameRoom:
    winner = []   #class variable
    
    def __init__(self):
        self.chulsu = Player("망치")
        self.younghee = Player("타짜")
        self.jimin = Player('미인')
        self.chulsu_flag = False
        self.younghee_flag = False
        self.jimin_flag = False
        
    def play(self):
        self._sysrandom = random.randint(1,11)
        while True:
            print('맞힐 숫자 : ' + str(self._sysrandom))
            GameRoom.winner.clear()
            self.chulsu.guess()
            self.younghee.guess()
            self.jimin.guess()
            print('망치 = ' + str(self.chulsu._myrandom))
            print('타짜 = ' + str(self.younghee._myrandom))
            print('미인 = ' + str(self.jimin._myrandom))
            if self._sysrandom == self.chulsu._myrandom : 
                self.chulsu_flag = True
                GameRoom.winner.append(self.chulsu)
            if self._sysrandom == self.younghee._myrandom : 
                self.younghee_flag = True
                GameRoom.winner.append(self.younghee)
            if self._sysrandom == self.jimin._myrandom : 
                self.jimin_flag = True
                GameRoom.winner.append(self.jimin)
            if self.chulsu_flag or self.younghee_flag or self.jimin_flag :
                print("맞히신 분이 계십니다.")
                for n in range(len(GameRoom.winner)):
                    print(GameRoom.winner[n])
                break
            else : 
                print('-' * 50)
                print('아무도 맞히신 분이 안계십니다.\n다시 게임을 시작합니다.')
                continue
            
            
            
            