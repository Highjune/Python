#readline()
with open ('서시.txt', 'rt', encoding = 'utf-8') as ptr:
    try :
        while 1 :#참일 경우(1이면 참)
            line = ptr.readline()
            if not len(line) : break
            print(line, end = '')    
                       
    except :
        print('Exception 발생')