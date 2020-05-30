#mylist = [1, 'Hello', True]
#print(type(mylist))   #<class 'list'>
#print(id(mylist))   #Python 변수들이 저장된 메모리 공간- Kernel
#mylist[1] = 'World'
#print(mylist)  #변경 가능, 상수가 아님
#mylist1 = mylist   #주소복사
#print(id(mylist), id(mylist1))



#mylist = [n for n in range(1, 6)]

#list 함수 1(넣고 빼기): append(), pop()
# mylist = []
# for n in range(1, 6): 
#     a = int(input('숫자 입력 : '))
#     mylist.append(a)
    
# print(mylist)

# mylist = [2,3,4,5,6]
# for n in range(1, 6):
#     print(mylist.pop())

#list 함수 2 : insert(), remove()
#mylist = ['Mango', 'Apple', 'Grape']
#mylist.insert(1, 'Melon')
#del mylist[4]   #IndexError
#mylist.remove('Melon')  #ValueError
#print(mylist)

# list 함수 3(packing / unpacking)
# mylist = ['Mango', 'Apple', 'Melon']  #packing
# #a, b, c = mylist     #unpacking
# #print(b)
# print(mylist.count('Melon'))

#mylist = [3,7,1,4,6,2,9]
# mylist = ['Mango', 'Apple', 'Melon']
# mylist.sort()
# print(mylist)
# mylist.reverse()
# print(mylist)

# def getLength(value):
#     return len(value)

#aaa = lambda value : len(value)
#print(aaa('Java'))

#mylist = ['Java', 'Python', 'jQuery', 'CSS', 'DB', 'MariaDB']
# #mylist.sort()
# #print([getLength(n) for n in mylist])
#mylist.sort(key = lambda value : len(value), reverse=True)
# print(mylist)


#def myfunction(value):
#    return value.lower()

# mylist = ['jAVA', 'cSS', 'JQUERY', 'hTML']
# mylist.sort(key=lambda value : value.lower())
# print(mylist)
# #
#print(myfunction('JAVA'))

# def getTotal(value):
#     return value[1]

# students = [['한지민', 287], ['김지민', 253], ['박지민', 300]]
# #students.sort(key = getTotal, reverse = True)
# students.sort(key = lambda value : value[0])
# print(students)
# for i in range(len(students) - 1):
#     for j in range(len(students) - 1):
#         if students[j][1] < students[j+1][1] :
#             mylist = students[j+1]
#             students[j+1] = students[j]
#             students[j] = mylist

# a = ['Java', 'Python', 'JavaScript', 'Vue', 'React'] 
# #print(a + b)
# a.extend(['된장찌게', '김치찌게'])
# print(a)

# a = 'Java', 'Python', 'JavaScript', 'Vue', 'React'
# b = 'Mango', 'Apple'
# mylist = list(b)
# print(type(mylist))  #<class 'list'>
# mylist.append('Grape')
# b = tuple(mylist)
# print(b)
# print(a[2])  #indexing
# print(a[::-1])  #slicing
# print(a + b)  #concat
# print(b * 3)  #repetition
# print(len(a))
# print('Mango' in b)

# a = 'Mango',
# print(type(a))

a = 5
b = 9
a, b = b, a
print(a, b)
# temp = a
# a = b
# b = temp
