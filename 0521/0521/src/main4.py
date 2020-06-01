with open('서시.txt', 'rt', encoding = 'utf-8') as ptr:
    try:
        while 1:
            content = ptr.read(10)
            if len(content) == 0 : break
            print(content, end = '')
    except :
        print('Exception 발생')