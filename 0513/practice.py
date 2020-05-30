#1. 
# name = '한지민'
# age = 24
# print('{}님의 나이는 {}살입니다.'.format(name, age))
# print('%s님의 나이는 %d살입니다.' % (name, age))
# print(name + '님의 나이는 ' + str(age) + '살입니다.')

#2. 
# a = int(input('첫번째 숫자 : '))
# b = int(input('두번째 숫자 : '))
# print('{} + {} = {}'.format(a, b, (a + b)))
# print('{} - {} = {}'.format(a, b, (a - b)))
# print('{} x {} = {}'.format(a, b, (a * b)))
# print('{0} / {1} = {2:.2f}'.format(a, b, (a / b)))
# print('{} / {}의 몫은 = {}'.format(a, b, (a // b)))
# print('{} / {}의 나머지는 = {}'.format(a, b, (a % b)))

#3.
str = 'Hello World'
mylist = str.split(' ')   #Hello     World
print(' '.join([mylist[1], mylist[0]]))

#4.
x = 'abcdef'
print(x[1:] + x[:1])

#5. 
x = 'abcdef'
print(x[::-1])

#6. 
temp = float(input("오늘의 온도 : "))
F = round((temp * 1.8) + 32, 2)
print('화씨온도 = ' + str(F))