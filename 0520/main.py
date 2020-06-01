#print('hello)

#if False:
#prin('hello')
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

class ValueCheck : 
    def calc(self):
        while True : 
            try:
                su = int(input('숫자만 입력해 주세요 : '))
            except : 
                print('숫자가 아닙니다.')
            else : 
                print(su / 5)
                print('숫자 맞습니다.')
                break

vc = ValueCheck()
vc.calc()