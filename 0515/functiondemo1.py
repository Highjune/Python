# def calcSum(start, stop):
#     total = 0    #지역변수
#     for n in range(start, stop + 1):
#         total += n
#     print('sum = ' + str(total))

# calcSum(1, 10)
# print('total = ' + str(total))

# val = 100
# def myfunc():
#     #global val = 5
#     global val
#     val = 5
#     print('In function val = ' + str(val))

# myfunc()
# print('Out function val = ' + str(val))


##Collection 용 함수
#1. enumerate(iterable[, start])
# data = [56,78, 90,100, 77]
# for n, d in enumerate(data, 1):
#     print(str(n) + '번째 학생의 성적 : ' + str(d))

#2. filter()
# def get_even(val):
#     return val % 2 == 0
    # mylist = []
    # for n in list:
    #     if n % 2 == 0 : mylist.append(n)
    # return mylist

# data = [56,78, 90,100, 77]
# #mylist = get_even(data)    
# #print(mylist)
# #mylist = filter(get_even, data)
# mylist = filter(lambda val : val % 2 == 0, data)
# print(type(mylist))   #<class 'filter'>
# print(list(mylist))

#3. zip()
# yoil = ['월요일', '화요일', '수요일', '목요일', '금요일']
# cook = ['짜장면', '짬뽕', '마파두부', '볶음밥', '잡채밥', '군만두', '김치찌게', '된장찌게']
# menu = zip(yoil, cook)
# # for y, c in menu:
# #     print(y + '의 음식은 ' + c + '입니다.')
# mydict = dict(menu)
# print('월요일 메뉴는 ' + mydict['월요일'])
# mydict['월요일'] = '삼선짜장'
# print('월요일 메뉴는 ' + mydict['월요일'])

#4. map()
def half(val):
    return val / 2
    # list = []
    # for a in val:
    #     list.append(a / 2)
    # return list

# data = [56,78, 90,100, 77]
# #mylist = half(data)
# for n in map(half, data):
#     print(n, end = '\t')

# for n in map(lambda a, b : a + b, [1,2,3,4,5], [10,20,30,40,50]):
#     print(n, end = '\t')

#4. Collection의 사본
# a = 3
# b = a
# print('a = ' + str(a) + ', b = ' + str(b))

# a = 5
# print('a = ' + str(a) + ', b = ' + str(b))

# a = [1,2,3]
# b = a
# print('a = ' + str(a) + ', b = ' + str(b))
# a = [4,5,6]
# print('a = ' + str(a) + ', b = ' + str(b))

# a = [1,2,3]
# b = a
# print('a = ' + str(a) + ', b = ' + str(b))
# a[1] = 100
# print('a = ' + str(a) + ', b = ' + str(b))

#완전한 복사 : copy(), 두 개의 list가 서로 완전히 독립적인 복사

# a = [1,2,3]
# b = a             #주소복사
# c = a.copy()  #값복사:shallow copy, 얕은복사
# d = a[:]        #값복사

# print(id(a)) #2336
# print(id(b)) #2336
# print(id(c)) #8864
# a[0] = 100
# print(b)
# print(c)
# print(d)

# alist = ['a', 'b']
# blist = [alist, 1, 2]
# clist = blist.copy()  #값복사

# clist[0][1] = 'c'
# print(alist)
# print(blist)


#5. deepcopy()

# import copy

# alist = ['a', 'b']
# blist = [alist, 1, 2]
# clist = copy.deepcopy(blist)   #값복사

# # clist[0][1] = 'c'
# # print(alist)
# # print(blist)

# print('alist == blist  ' + str(alist is blist))
# print('blist == clist  ' + str(blist is clist))
# print('alist == clist  ' + str(alist is clist))

a = 1
b = a
print('a == b --> ' + str(a is b))
b = 5
print('a == b --> ' + str(a is b))