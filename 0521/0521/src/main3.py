with open('서시.txt', 'rt', encoding = 'utf-8') as ptr:  #File Pointer ptr도 Collection이다.
    try:
        for n in ptr:
            print(n, end = '')
    except FileNotFoundError :
        print('File Not Found')
    except Exception as e:
        print('Exception 발생, ', e.args[0])
    
    