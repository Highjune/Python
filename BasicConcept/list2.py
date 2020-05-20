# mylist = [1, 'Hello', True]
# print(type(mylist))  #<class 'list'>
# print(id(mylist)) #Python 변수들이 저장된 메모리 공간 - kernel
# mylist[1] = 'World' #replace
# print(mylist)  #변경 가능, 상수가 아님
# mylist1 = mylist  #주소복사
# print(id(mylist), id(mylist1))

# mylist = []
# for n in range(1, 6):
#     mylist.append(n)

# mylist = [n for n in range(1, 6)]

#list 함수1(넣고 빼기) : append(), pop()
#append()
# mylist = []
# for n in range(1, 6):
#     a = int(input('숫자 입력 : '))
#     mylist.append(a)
# print(mylist)

#pop()
# mylist = [2, 3, 4, 5, 6]
# for n in range(1, 6):
#     print(mylist.pop())


#list 함수2 : insert(), remove()
# mylist = ['Mango', 'Apple', 'Grape']
# del mylist[1] #index로 지우기
# del mylist[4] #IndexEror (index를 벗어났으니)
# mylist.remove('Mango') #값으로 지우기
# mylist.remove('Melon') #ValueError (없는 값 지우려고 하면)
# print(mylist)


#list 함수3 : packing / inpacking
# mylist = ['Mango', 'Apple', 'Melon'] #packing
# a, b, c = mylist #unpacking
# print(b)
# print(mylist.count('Melon'))


# mylist = [3, 7, 1, 2, 3, 6, 2]
# mylist.sort() #오름차순 정렬
# print(mylist)
# mylist.reverse()
# print(mylist) #내림차순 정렬

#문자열도 유니코드이므로 정렬 가능
# mylist = ['Mango', 'Apple', 'Melon']
# mylist.sort() #오름차순 정렬
# print(mylist)
# mylist.reverse()
# print(mylist) #내림차순 정렬


#함수
# def getLength(value):
#     return len(value)

# aaa = lambda value : len(value)
# print(aaa('Java'))

# mylist = ['Java', 'Python', 'jQuery', 'CSS', 'DB', 'MariaDB']
# mylist.sort() #그냥 정렬하면 index기준
# print([getLength(n) for n in mylist])
# mylist.sort(key=getLength) #key는 sort의 기준
# mylist.sort(key=lambda value : len(value), reverse=True) #람다로
# print(mylist)


# mylist = ['Java', 'Python', 'jQuery', 'CSS', 'DB', 'MariaDB']
# mylist.sort(key=lambda value : len(value), reverse=True) #람다로
# print(mylist)


# def myfunction(value):
#     return value.lower()

# mylist = ['jAVA', 'cSS', 'JQUERY', 'hTML']
# mylist.sort(key=lambda value : value.lower())
# print(mylist)

# lambda value : value.lower()
# print(myfunction('JAVA'))


# students = [['한지민', 257],['김지민', 287],['박지민', 300]]
# for n in range(len(students)-1):
#     for j in range(len(students)-1):
#         if students[j][1] < students[j+1][1] :
#             mylist = students[j+1]
#             students[j+1] = students[j]
#             students[j] = mylist

# print(students)


# students = [['한지민', 257],['김지민', 287],['박지민', 300]]
# for n in range(len(students)-1):
#     for j in range(len(students)-1):
#         if students[j][1] < students[j+1][1] :
#             mylist = students[j+1]
#             students[j+1] = students[j]
#             students[j] = mylist
# print(students)

# def getTotal(value):
#     return value[1]

# students = [['한지민', 257],['김지민', 287],['박지민', 300]]
# # studnets.sort(key=getTotal, reverse = True)
# students.sort(key=lambda value : value[1]) #람다로 변환
# print(students)

# a = ['Java', 'Python', 'JavaScript', 'Vue', 'React']
# b = ['된장찌개', '김치찌개']
# print(a+b)

# a = ['Java', 'Python', 'JavaScript', 'Vue', 'React']
# a.extend(['된장찌개', '김치찌개'])
# print(a)

# a = ('Java', 'Python', 'JavaScript', 'Vue', 'React')
# b = ('Mango', 'Apple')
# mylist = list(b)
# print(type(mylist)) #<class 'list'> list가 됨
# mylist.append('Grape') #Grape추가
# b = tuple(mylist)
# print(b)
# print(a[2])     #indexing
# print(a[::-1])  #slicing
# print(a+b)
# print(b*3)
# print(len(a))
# print('Mango' in b)

# a = 'Mango',
# print(type(a))

#값 교체
a = 5
b = 9
a, b = b, a
print(b, a)

