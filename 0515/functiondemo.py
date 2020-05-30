# def change(val):
#     print(id(val))
#     #val = {'name':'박지민', 'age' : 34}
#     val['name'] = '박지민'
#     print('In function val = ' + str(val))


# before = {'name':'한지민', 'age' : 24}
# print(id(before))
# change(before)
# print('before = ' + str(before))

# def myfunction(*args):  #packing
#     sum = 0
#     for n in args:
#         sum += n
#     print('sum = ' + str(sum))

# mylist = (1,2,3)
# myfunction(*mylist)  #unpacking
# #myfunction(1,2,3,4,5)


# def myfunction(**args):  #packing
#     for (k, v) in args.items():
#         print(str(k) + ' --->' + str(v))

# mydict = {'name':'한지민', 'age' : 24, 'address' : '서울시 강남구'}
# myfunction(**mydict)  #unpacking

# def myfunction(name, *args, age = 20, **args1):
#     print('name = ' + name)
#     print('age = ' + str(age))
#     for n in args:
#         print(n, end = '\t')
#     print()
#     for (k, v) in args1.items():
#         print(str(k) + ' --> ' + str(v))

# myfunction('한지민', 100,78,90, age = 24, address='서울시 강남구', gender = 'Female')

# def get_even(mylist):
#     a = []
#     for n in mylist:
#         if n % 2 == 0 : a.append(n)

#     return a

# a = get_even   #<class 'function'>
# #print(type(a))
# print(a([1,3,4,5,8,2,3]))

# import math

# def mypower(x, y):
#     return math.pow(x, y)

# #print(mypower(2, 6))
# a = lambda x, y : math.pow(x, y)
# print(a(2, 8))

def swap(a, b):
    return b, a

x, y = swap(5, 9)
print('x = ' + str(x) + ', y = ' + str(y))