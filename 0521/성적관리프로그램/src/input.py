#input.py
from student import Student 

def myinput(mylist):
    num = 0
    while True :
        num = num + 1 
        print(str(num) + '번째 학생 입력 : ')
        hakbun = input('학번 : ')
        name = input('이름 : ')
        kor = int(input('국어 : '))
        eng = int(input('영어 : '))
        mat = int(input('수학 : '))
        s = Student(hakbun, name, kor, eng, mat)
        mylist.append(s)
        y_n = input('Again(y/n) ? : ')
        if y_n == 'y' : continue
        else : break
        