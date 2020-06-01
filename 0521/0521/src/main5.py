with open('서시.txt', 'rt', encoding = 'utf-8') as ptr:
    try:
        mylist = ptr.readlines()   #readlines()도 collection이다.
        no = 1
        for n in mylist:
            print(no, ':', n, end = '')
            no = no + 1
            
    except :
        print('Exception 발생')