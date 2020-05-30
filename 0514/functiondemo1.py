#Required Argument
# def printInfo(name, age):
#     print('name = %s, age = %d' % (name,age))


# printInfo(age = 24, name = '한지민')   #Keyword Argument

# def print_student(hakbun, name, tot, avg, grade):
#     print('{} {} {} {} {}'.format(hakbun, name, tot, avg, grade))

# print_student(grade = 'A', name = '한지민', avg = 89.5, hakbun = '2010-01', tot = 372)


# def printInfo(name = '한지민', age):
#     print('name = %s, age = %d' % (name,age))

# #printInfo(age = 24, name = '한지민')   #keyword argument
# printInfo('한지민')
# printInfo('박지민', 34)

#default argument
# def printInfo(name, age = 20, address = '서울시 강남구'):
#     print('name = {}, age = {}, address = {}'.format(name, age, address))

# printInfo('한지민', 24, '경기도 수원시')
# printInfo('박지민')
# printInfo('김지민', 34)

# def myprint(su, *args):   #variable-length argument
#     print(su)
#     print('-' * 50)
#     for num in args:
#         print(num, end = '\t')
#     print()

# myprint(True)
# myprint((6,7,8), [1,2,3,4,5],False, 89.5)
# myprint('Hello', 2020)

#keyword variable-length argument
#def myprint(**args):      

# def myprint(start, step = 1, *stop):
#     for n in range(start, stop, step):
#         print(n, end = '\t')
#     print() 

# #myprint(1, 10, 2)  #requirement argument
# #myprint(step = 2, stop = 10, start = 1)  #keyword argument
# myprint(stop = 10, start = 5)   #default argument

# def myprint(**args):
#     print('start = ' + str(args['start']))
#     print('stop = ' + str(args['stop']))
#     print('step = ' + str(args['step']))


# myprint(start = 1, stop = 10, step = 2)

# def printInfo(**args):
#     print(args.keys())

# printInfo(이름 = '한지민', 나이 = 24)
# printInfo(국어 = 100, 영어 = 90, 수학 = 78)
# printInfo(키 = 184.7, 몸무게 = 68.2)

# def printInfo(hakbun, name, *subjects, **args):
#     print('hakun = {}, name = {}'.format(hakbun, name))
#     sum = 0
#     for n in subjects:
#         sum += n
#     print("총점 = {}".format(sum))
#     for (k, v) in args.items():
#         print(k, v)

# #printInfo(name = '한지민', hakbun = '2020-01')  #keyword argument
# #printInfo('2019-05', '김지민')  #required argument
# printInfo('2020-01', '한지민', 100, 78, langauge = ('Java', 'Python'), gender = 'female')
# printInfo('2020-02', '김지민', 90, 88, 100, hobby = ['낚시', '등산', '여행'])

# def add(a, b): return a + b

# def subtrack(a, b): return a - b

# def multiply(a, b): return a * b

# def divide(a, b):  return a / b

# aaa = lambda a, b : a + b
# print(aaa(5, 9))
# aaa = lambda a, b : a * b
# print(aaa(5, 9))

#scores = [89, 99, 78, 65, 100]
# su = 1
# for num in scores : 
#     print(str(su) + '번째 학생의 성적 : ' + str(num))
#     su = su + 1
# for num in range(len(scores)):
#     print(str(num + 1) + '번째 학생의 성적 : ' + str(scores[num]))

# scores = [89, 99, 78, 65, 100]
# # for (k, v) in enumerate(scores) :
# #     print(str(k+1) + '번째 학생의 성적 : ' + str(v))

# for (k, v) in enumerate(scores, 1) : 
#     print(str(k) + '번째 학생의 성적 : ' + str(v))


# def flunk(score):
#     return score < 60

scores = [89, 39, 28, 45, 100]
for num in filter(lambda s : s < 60, scores):
    print(num)