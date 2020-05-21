with open('0521.txt', 'at', encoding='utf-8') as ptr: #at의 a는 append
    try :
        while True :
            message = input("남기실 말씀(quit : 끝) : ")
            if message == 'quit' : break
            ptr.writelines(message + '\n')
    except :
        print('Exception 발생')
    else :
        print('Save Successfully')