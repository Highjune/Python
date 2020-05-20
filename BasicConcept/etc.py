# for i in range(1, 11):
#     for j in range(i):
#         print('*', end = '')
#     print()


# str = 'Hello, world'
# print(str[0])
# print(str[1])
# print(str[-1])

# str = 'Hello, world'
# print(str[1:4]) #1~3
# print(str[:4]) #0~3
# print(str[5:]) #5 ~ 끝까지
# print(str[:]) #처음 ~ 끝까지


# now = '2020-05-12 12:18:33'
# date = now[:10] #0~9
# time = now[11:] #11~끝
# print('날짜 = ' + date)
# print('시간 = ' + time)


# str = '죽는 날까지 하늘을 우러러'
# str += '한 점 부끄럼이 없기를'
# str += '잎세에 이는 바람에도 나는 괴로와 했다'
# print(str)


# str = '죽는 날까지 하늘을 우러러 \
#         한 점 부끄럼이 없기를 \
#         잎세에 이는 바람에도 나는 괴로와 했다'
# print(str)


# a = None
# a = 5
# print(type(a)) #<class 'int'>
# a = 'Hello'
# print(type(a)) #<class 'str'>
# a = True
# print(type(a)) #<class 'bool'>
# a=3.14
# print(type(a)) #<class 'float'>


# mylist = list()
# while (str := input('입력 : ')) != 'quit' :
#     mylist.append(str)

# print(mylist)
    

# print(aaa:=true)


# a=b=c=1
# a, b, c = 'june', 34.1 , 56


# age = 24
# print('나이 =' + str(age) + '살입니다.')

# name = 'june'; #object
# print(type(name)) #<class 'str'>

# age = 24
# print(type(age)) #<class 'int'>


# name = 'june hi';
# print(name.title())
# print(name.upper())
# print(name.lower())


# mylist = [4, 34.1, True, ['apple', 'banana', 'Grape']]


# mylist  = list()
# for i in range(1, 6):
#     mylist.append(input('Enter a fruits: '))
# print(mylist)

# mylist  = list()
# for i in range(1, 6):
#     mylist.append(input('Enter a fruits: '))
# print(mylist[0])  #0 1 2 3 4
# print(mylist[-1]) #-5 -4 -3 -2 -1

# mytuple = ('사과', '배', '딸기', '수학')
# print(mytuple[:3])
# print(mytuple[3:])

# car = {'name' : 'Sonata', 'price':25000000, 'maker':'Hyundai'}
# print(car.keys())
# print(car.values())

# for i in range(ord('A'), ord('Z') + 1):
#     print(chr(i), end=',')


# sum = 0
# for i in range(1, 100):
# 	sum += i
# 	print('sum = ' + str(sum));

# for i in range(1, 10):
# 	print('7 x' + str(i) + ' = ' + str(7*i))



#구구단
for i in range(1, 10) :
    for j in range(2, 10) :
        print(str(j) + ' x ' + str(i) + ' = ' + str(j*i), end = '\t')
    print()


#break
#x는 1부터 100까지 3씩 증가하고
#y는 100부터 1까지 2씩 감소할 때
#결국 x와 y는 서로 교차할 것이다.
#이 때 교차되는 최초의 x, y의 값은?
for i in range(1, 100, 3) :
    for j in range(100, 1, -2):
        pass;

