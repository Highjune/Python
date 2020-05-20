# print('hello)

# if False:
    # prin('hello')

# try : 
#     a = int(input('첫번째 숫자 : '))
#     b = int(input('두번째 숫자 : '))
#     result = a / b
# except : 
#     print('오류발생')
# else :
#     print('result = ' + str(result))


# a = int(input('숫자만 넣으세요 : '))
# print(a)

#################################
# 실습)숫자만 입력받는 ValueCheck class를 완성하시오. 멤버 메소드는 calc()이고, 
# input()을 통해 값을 입력받고 숫자 여부는 calc()가 결정한다. 
# 만일 숫자가 아니면 계속 숫자를 입력할 때가지 무한 loop로 처리한다. 

# class ValueCheck :
#     def calc(self):
#         while True :
#             try :
#                 su = int(input('숫자만 입력해 주세요 : '))
#                 print(su / 5)
#                 print('숫자 맞습니다.')
#                 break
#             except : 
#                 print('숫자가 아닙니다.')

#else를 넣어서
class ValueCheck :
    def calc(self):
        while True :
            try :
                su = int(input('숫자만 입력해 주세요 : '))
            except : 
                print('숫자가 아닙니다.')
            else : 
                print(su / 5)
                print('숫자 맞습니다.')
                break

vc = ValueCheck()
vc.calc()

