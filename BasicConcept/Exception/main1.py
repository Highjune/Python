# while True : 
#     try:
#         su = int(input('숫자만 입력하세요 : '))
#         print(su / 4);
#         break
#     # exception종류 알고 싶을 때
#     except Exception as ex:  #1. Exception으로 받아서
#         print('숫자가 아닙니다. 숫자를 넣어주세요')
#         print(type(ex)) #2. type찍어보기



while True : 
    try :
        su = int(input('숫자만 입력하세요 : '))
        print(su / 4);
        break
    # except FileNotFoundError : #명확한 에러 종류로 받지 못한다면 에러발생.
    except Exception : #제일 부모형 Exception으로 받으면 에러 종류를 모르더라도 다 받을 수 있다.
        print('숫자가 아닙니다. 숫자를 넣어주세요')
        
