# mylist = [1,2,3,4,5,6,7,8,9,10]
# myotherlist = [i ** 2 for i in mylist]
# # for i in mylist:
# #     myotherlist.append(i)

# print(myotherlist)

#print([n ** 2 for n in range(1, 11) if n ** 2 > 30])

#mylist = [56, 3.14, True, [1,2,3], (4,5,6), {'name':'Sonata'}, 67, 89.5]
#print([n for n in mylist if type(n) == int])

#mylist = [34, -36, 12, -6, 9, 3, -5, -2]
#print([n for n in mylist if n > 0])
#print([n if n>0 else 0 for n in mylist])

# mylist = [[1,2,3], [4,5,6], [7,8,9]]
# print([n for row in mylist for n in row])

# a = 0xABCD
# b = 0o21
# c = 0b1001010
# #print(hex(a))
# print('{0:#x}'.format(a))
# print('{0:#o}'.format(a))
# print('{0:#b}'.format(a))

# a = int('345')  #345
# b = int(89.5)   #89

# a  = float('89.5')    # 89.5
# b = float(89)   #89.0

# avg = 89.56789
# print("avg = %.2f" % avg)
# print("avg = {0:.2f}".format(avg))
# avg1 = round(avg, 2)
# print(avg1)

# avg = 87.56789
# print(round(avg))  #소수점 첫째 자리
# print(round(avg, 0))  #소수점 첫째 자리
# print(round(avg, -1))  #정수 첫째 자리
# print(round(avg, 2))  #소수점 둘째 자리까지 표시, 셋째 자리에서 반올림 여부


# import random

# print(choice([1,2,3,4,5]))
#print('-----------------------------------------------------------')
#print('-' * 40)
# a = 'Hello'
# b = 'Python'
#print(a[20:50])
# print(a + b)
# print(a * 4)
# print(a[2])
# print(b[2:6])
# print(len(a))
# print('e' in a)

#slice([start : stop : step])
# a = 'Hello, World'
# print(a[:])  # 전체 문자열
# print(a[::-1])
# print(a[::2])

# str 함수 1(검색) : find(), index(), count(), len()
# str = 'Hello, World'
# print(str.find('w'))   # -1
# print(str.find('W'))
# print(str.index('W'))
# #print(str.index('w'))  exception 발생
# print(str.count('w'))
# print(str.count('W'))
# print(str.count('l'))
# for ch in range(len(str)):
#     print(str[ch], end = ', ')

# str 함수 2(조사) : in, startsWith(), endsWith(), is~()
# str = 'jimin.jpg'
# print(str.endswith('.jpg')) 
# print(str.isdigit())
# print(str.isalpha())
# print(str.isalnum())

# str 함수 3(변경) : title(), capitalize(), upper(), lower(), strip(), lstrip(), rstrip()
#str = 'hello, world'
#print(str.title())
#print(str.capitalize())
# str = '               Hello, World         '
# print(str.lstrip())
# print(str.rstrip())
# print(str.strip())

# str 함수 4(packaging/unpackaging) : join(), split()
#mylist = ['Mango', 'Apple', 'Grape', 'Melon']
#mylist.join('-') in Java
#str = '-'.join(mylist)  #특히 조심할 것, list --> string
#print(str)

# str = '2020-05-13'
# mylist = str.split('-')   #string --> list
# print([n for n in mylist])

# str 함수 5(replace) : replace(), ljust(), rjust(), center()
#str = 'Hello'
#str[0] ='C'
#print(str)  #exception 발생
# print(str.replace('H', 'C', 1))
# str = str.replace('H', 'C', 1)
# print(str)

# print(str.rjust(20))
# print("{0:>20s}".format(str))
# print("%20s" % str)
# print(str.ljust(20, 'a'))
# print("{0:<20s}".format(str))
# print("%-20s" % str)
# print(str.center(20, 'a'))

