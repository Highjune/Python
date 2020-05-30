#fourth.py

# for i in range(1, 11):
#     for j in range(i):
#       print('*', end = '')
#     print()

#str = 'Hello, World'
# print(str[0])
# print(str[1])
# print(str[-1])
# print(str[1:4])  #1 ~ 3
# print(str[:4])   # 0 ~ 3
# print(str[5:])   # 5 ~ 끝까지
# print(str[:])     #처음부터 ~ 끝까지


# now = '2020-05-12 12:18:33'
# date = now[:10]   # 0 ~ 9
# time = now[11:]   # 11 ~ 끝
# print('날짜 = ' + date)
# print('시간 = ' + time)

# path = r'C:\temp\new.txt'   #raw string
# path = 'C:/temp/new.txt'
# print(path)

# str = """죽는 날까지 하늘을 우러러
# 한 점 부끄럼이 없기를
# d
# fds
# ds
# fsd
# ds
# sd
# fds
# fds
# fds
# 잎세에 이는 바람에도 나는 괴로와 했다"""
# print(str)

# a = None
# a = 5
# print(type(a))    #<class 'int'>
# a = 'Hello'
# print(type(a))     #<class 'str'>
# a = True
# print(type(a))     #<class 'bool'>
# a = 3.14
# print(type(a))     #<class 'float'>


# mylist = list()
# while (str := input('입력 : ')) != 'quit' :
#     mylist.append(str)

# print(mylist)

#print(aaa := True)

#print(43.2 - 43.1)

#a = b = c = 1
# a, b, c = 'John', 34.1, 56
# print(a)
# print(b)
# print(c)

# name = input('Name : ');    age = int(input('Age : '));   kor = int(input('Korean : '));
# eng = int(input('English : '));  mat = int(input('Math : '));
# sum = kor + eng + mat;    avg = sum / 3;
# grade = None
# if 90 <= avg <= 100 : grade = 'A'
# elif 80 <= avg < 90 : grade = 'B'
# elif 70 <= avg < 80 : grade = 'C'
# elif 60 <= avg < 70 : grade = 'D'
# else : grade = 'F'
# print('이름 = {0}, 나이 = {1}'.format(name,age))
# print('국어 = {0}, 영어 = {1}, 수학 = {2}, 총점 = {3}, 평균 = {4}, 평점 = {5}'
#          .format(kor, eng, mat, sum, avg, grade))


# print(5 / 2)  #실수나누기
# print(5 // 2)   #정수나누기


# a = 5
# print('a = {}'.format(a))

# del a
# print('a = {}'.format(a))

# a = 128
# print(a)
# print(hex(a))
# print(oct(a))
# print(bin(a))

# a = 0xABCD
# b = 'Hello'
# print(str(a) + b)

# age = 24
# print('나이 = ' + str(age) + '살입니다.')

# name = 'michael jackson';   #Object
# print(name.title())
# print(name.upper())
# print(name.lower())
# #print(type(name))   #<class 'str'>

# mylist = [4, 34.1, True, ['Mango', 'Apple','Grape']]


# age = 24
# print(type(age))   #<class 'int'>

# mylist = list()
# for i in range(1, 6):
#     mylist.append(input('Enter a fruits : '))

# print(mylist[0])
# print(mylist[-1])

# mytuple = ('사과', '배', '딸기', '수학', '복숭아')
# print(mytuple[:3])
# print(mytuple[3:])

# car = {'name': 'Sonata', 'price':25000000, 'maker':'Hyundai'}
# print(car.keys())
# print(car.values())

#print(chr(97))
# print(ord('A'))

# a = 10
# b = 10
#print(id(a))   #140719694600128
#print(id(b))   #140719694600128
# if( a is b) :  print('Equals')
# else : print('Different')

# b = 15
# if( a is b) :  print('Equals')
# else : print('Different')
#print(id(a))   #140719694600128
#print(id(b))   #140719694600288

# a = 230
# b = a
# print(id(a))
# print(id(b))

#for i in [1,2,3,4,5] :
# sum = 0
# for i in range(1, 101) : 
#     sum += i 
# print('sum = ' + str(sum))

# for i in range(1, 10):
# #     print('7 x ' + str(i) + ' = ' + str(7 * i))
# print('##############구구단#############')
# for i in range(1, 10) :
#     for j in range(2, 10):
#         print(str(j) + ' x ' + str(i) + ' = ' + str(j * i), end = '\t')
#     print()

#x는 1부터 100까지 3씩 증가하고
#y는 100부터 1까지 2씩 감소할 때
#결국 x와 y는 서로 교차할 것이다. 
#이때 교차되는 최초의 x, y의 값은?
# for i in (1, 100):
#     if i == 5:
#         pass

#-5 ~ 256
# a = 255
# print(a == 255)   #값비교
# print(a is 255)   #주소비교
# a += 1
# print(a == 256)   #값비교
# print(a is 256)   #주소비교
# a += 1
# print(a == 257)   #값비교
# print(a is 257)   #주소비교

a = -5
print(a == -5)  #값비교
print(a is -5)  #주소비교
a -= 1
print(a == -6)  #값비교
print(a is -6)  #주소비교