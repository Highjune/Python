while True : 
    try :
        su = int(input('숫자만 입력하세요 : '))
        print(5 / su)
        break
    except Exception :
        print('Exception')
    except ZeroDivisionError :
        print('ZeroDivisionError')
    except ValueError :
        print('ValueError')