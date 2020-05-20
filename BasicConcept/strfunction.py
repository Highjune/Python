# print('-'*40)
# a='Hello'
# b='June'
# print(a+b)
# print(a*b)
# print(a[2])
# print(b[2:6])
# print(len(a))
# print('e' in a)

# print(a[20]) // 에러남. 범위가 넘어서
# print(a[20:50]) 

#slice([start : stop : step])
# a = "Hello, World"
# print(a[:]) #전체 문자열
# print(a[::-1]) #뒤에서부터
# print(a[::2]) #한칸씩 건너 뛰어서


# str 함수 1  : find(), index(), count(), len()
# str = 'Hello, World'
# print(str.find('w')) #없으면 -1
# print(str.find('W'))


# print(str.index('w'))  #에러 메시지를 알려줌 
# print(str.index('W'))


# print(str.count('w'))
# print(str.count('W'))


# for ch in range(len(str)): #ch에는 11이 들어감(str의 길이)
#     print(ch, end = ',')


# for ch in range(len(str)): #ch에는 11이 들어감(str의 길이)
#     print(str[ch], end = ',')


#str 함수 2 (조사) : in, startsWith(), endWith(), is~()
# str = '허강준.jpg'
# print(str.endswith('.jpg'))
# print(str.isdigit())
# print(str.isalpha())
# print(str.isalnum())


#Str의 함수3(변경) - title(), capitalize(), upper(), lower(), strip()
# str = 'hello, world'
# print(str.title())  #단어 첫 글자 대문자
# print(str.capitalize()) #문장의 첫 글자 대문자

# str = '         Hello, World'
# print(str.lstrip())
# print(str.rstrip())
# print(str.strip())


# Str의 함수4 - packaging/unpackaging : join(), split()
# mylist = ['Mango', 'Apple', 'Grape', 'Melon']
#mylist.join('-') in java (자바에서는 주체가 앞으로 온다)
#파이썬은 조인할 것이 앞으로 온다
# str = '-'.join(mylist)
# print(str)

# str = '2020-05-13'
# mylist = str.split('-') #String -> list
# print([n for n in mylist])

# Str의 함수5(replace) : replace(), ljist(), rjust(), center()
# str = 'Hello'
# str[0] = 'C'
# print(str) #exception 발생

# str = 'Hello'
# # print(str.replace('H', 'C'))
# print(str.replace('H', 'C', 1))
# str = str.replace('H', 'C', 1)
# print(str)


# str = 'Hello'
# print(str.rjust(20))
# print("{0:>20s}".format(str))


str = 'Hello'
print(str.rjust(20))
print("{0:>20s}".format(str))
print("%20s" % str)
print(str.ljust(20, 'a'))
print("{0:<20s}".format(str))
print("%-20s" % str)


# str = 'Hello'
# print(str.center(20, 'a'))
