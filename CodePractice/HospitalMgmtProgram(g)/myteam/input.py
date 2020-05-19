#input.py

from hospital import Hospital

def myinput(mylist):
    num = 0
    while True:
        num = num + 1
        print("<" + str(num) + '번째 입력>')
        num = int(input('번호 :'))
        code = input('진료코드:')
        ibwonilsu = int(input('입원일수:'))
        age = int(input('나이 :'))        
        a = Hospital(num,code,ibwonilsu,age)
        mylist.append(a)
        i_o = input('Again(i/o) ? :')
        if i_o.upper() == 'I' : continue
        else : break
        
        