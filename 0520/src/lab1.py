while True:
    try:
        first = float(input('첫번째 숫자를 입력하세요 : '))
        second = float(input('두번째 숫자를 입력하세요 : '))
        print("입력한 숫자는 {}와 {}입니다.".format(first, second))
        print('{}을 {}로 나누면  {}입니다.'.format(first , second, (first /second)))
        break
    except ValueError:
        print('유효한 숫자가 아닙니다. 다시 시도하세요.')
    except ZeroDivisionError : 
        print('0으로 나눌 수 없습니다. 다시 시도하세요.')