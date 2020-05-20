while True:
    try:
        su = int(input('숫자만 입력하세요'))
    except Exception as ex:
        print('Error 유형 : ' + ex.__class__.__name__)
        print('Error 유형 : ', type(ex))
        print('Error Message : ', ex.args)
        print('기타 Message : ', ex)
    else :
        print(su/5)
        print('입력하신 유효한 숫자는 {}입니다.'.format(su))
        break
    finally :
        print('Program is Over...')

