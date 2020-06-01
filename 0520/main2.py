while True :
    try:
        su = in(input('숫자만 입력하세요 : '))
        print(5 / su)
        break
    except ValueError : 
        print('ValueError')
    except ZeroDivisionError : 
        print('ZeroDivisionError')
    except TypeError : 
        print('TypeError')