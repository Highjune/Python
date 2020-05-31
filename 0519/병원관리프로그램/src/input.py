#input.py
from patient import *

def myinput(mylist):
    num = 0
    while True:
        num = num + 1
        print('<<' + str(num) + '번째 환자입력>>')
        bunho = int(input('번호 : '))
        code = input('진료코드 : ')
        days = int(input('입원일수 : '))
        age = int(input('나이 : '))
        mylist.append(Patient(bunho, code, days, age))
        
        i_o = input('입력/출력(I/O)? : ')
        if i_o.upper() == 'I' : continue
        else : break