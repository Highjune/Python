#read() - 처음부터 끝까지 한 번에 읽어들임
# with open ('서시.txt', 'rt', encoding = 'utf-8') as ptr:
#     try :
#         print(ptr.read(10))
#     except :
#         print('Exception 발생')

#반복문으로 read

with open ('서시.txt', 'rt', encoding = 'utf-8') as ptr:
    try :
        while 1 : #1은 참, 0은 거짓
            content = print(ptr.read(10))
            if len(content) == 0 : break       
            print(content, end = '')            
    except :
        print('Exception 발생')
        
        