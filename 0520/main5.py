while True :
    try:
        su = int(input('숫자만 입력하세요 : '))
        print(5 / su)
        break
    except ZeroDivisionError : 
        print('ZeroDivisionError')
    except ValueError : 
        print('ValueError')
    except Exception : 
        print('Exception')
    finally:
        print('항상 수행함.')