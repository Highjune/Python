while True : 
    try:
        su = int(input('숫자만 입력하세요 : '))
        print(4 / su);
        break
    except Exception as ex:
        print('어쨌든 오류발생 = ', type(ex))