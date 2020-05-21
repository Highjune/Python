#readlines()
#여러 줄을 한 번에 읽는 방식
with open ('서시.txt', 'rt', encoding = 'utf-8') as ptr:
    try :
        mylist = ptr.readlines()
        no = 1
        for n in mylist:
            print(no, ':', n, end='')
            no = no + 1            
                       
    except :
        print('Exception 발생')