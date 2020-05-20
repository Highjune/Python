while True : 
    try :
        su = int(input('숫자만 입력하세요 : '))
        print(5 / su)
        break
    except (ValueError, ZeroDivisionError) :
        print('유효하지 않은 숫자입니다.')