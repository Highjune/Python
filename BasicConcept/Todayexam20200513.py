# 1. 이름과 나이 변수를 다음 형식으로 출력되도록 format() 함수를 이용해서 형시고하하기
# name = '한지민'
# age = 24
# 한지민님의 나이는 24살입니다.

# 나의 답 : print("{}님의 나이는 {}살입니다.".format(name, age))   #{}의 순서가 동일하면 {0}, {1} 이런식으로 꼭 안해도 된다.
# 선생님 답1 : print("{}님의 나이는 {}살입니다.".format(name, age))
# 선생님 답2 : print('%s님의 나이는 %d살입니다.' % (name, age))
# 선생님 답3 : print(name + '님의 나이는' + str(age) + '살입니다.')



# 2 두 정수를 입력받아 두 수의 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지를 출력하기

# a = int(input('첫번째 수 : '))
# b = int(input('두번째 수 : '))
# print('{0} + {1} = {2}'.format(a, b, a+b))
# print('{0} - {1} = {2}'.format(a, b, a-b))
# print('{0} x {1} = {2}'.format(a, b, a*b))
# print('{0} / {1} = {2}'.format(a, b, a/b))
# print('{0} / {1}의 몫은 = {2}'.format(a, b, a//b))
# print('{0} / {1}의 나머지는 = {2}'.format(a, b, (a%b)))

# {}안에 숫자 안 써도 된다.
# print('{} + {} = {}'.format(a, b, a+b))
# print('{} - {} = {}'.format(a, b, a-b))
# print('{} x {} = {}'.format(a, b, a*b))
# print('{} / {} = {}'.format(a, b, a/b))
# print('{} / {}의 몫은 = {}'.format(a, b, a//b))
# print('{} / {}의 나머지는 = {}'.format(a, b, (a%b)))




# 3. 문자열의 분리하기와 합치기 기능을 이용하여 'Hello World'를 'World Hello'로 출력하기
# str = "Hello World"
# a = str.split(' ')[0]
# b = str.split(' ')[1]
# list = [b, a]
# result = ' '.join(list)
# print(result)
# print(b + ' '+ a) #이렇게 해도 됨

# (선생님답)
# str = "Hello World"
# mylist = str.split(' ')
# print(' '.join([mylist[1], mylist[0]]))



# 4. x = 'abcdef'를 bcdefa'로 출력하기(문자열 slicing 기능 이용할 것)
# x = 'abcdef'
# y = x[1:] + x[0:1]
# print(y)

# (선생님답)
# x = 'abcdef'
# print(x[1:] + x[:1])




# 5. x = 'abcdef'를 'fedcba'로 출력하기
# x = 'abcdef'
# print(x[::-1])



# 6. 오늘의 온도를 섭씨온도로 입력받아 다음 조건에 맞게 화씨온도로 변환하기
# 1) 화씨온도는 소수점 두 번재 자리까지 출력
# 2) 변환공식(C: 섭씨, F:화씨)
# C = (F - 32) / 1.8
# F = (C * 1.8) + 32

# temp = float(input("오늘의 온도 : "))
# F = round((temp * 1.8) + 32, 2)
# print('화씨온도 = ' + str(F))


