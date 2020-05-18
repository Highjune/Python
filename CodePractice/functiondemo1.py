#Required Argument
# 에러남, age를 안 넣었으니까
# def printInfo(name, age):
#     print('name = %s, age=%d' % (name, age))

# printInfo('한지민')


#Keyword Argument
# def printInfo(name, age):
#     print('name = %s, age=%d' % (name, age))

# printInfo(age = 24, name= '한지민') 

# def print_student(hakbun, name, tot, avg, grade):
#     print('{} {} {} {} {}'.format(hakbun, name, tot, avg, grade))

# print_studnet(grade='A', name='한지민', avg=89.5, hakbun='2010-01', tot=372)

#Default Argument
# def printInfo(name, age=20):
#     print('name = %s, age=%d' % (name, age))

# printInfo('한지민')
# printInfo('박지민', 34)

# def printInfo(name, age=20, address):
#     print('name = {}, age = {}, address = {}'.format(name, age, address))

# printInfo('한지민', '서울시 강남구') 
# 우측부터 채워나가야 된다. 왼쪽이랑 중간은 default Argument를 줄 수 없다.

#경우에 따라 기본인자 3가지 방법으로 호출 가능
# def printInfo(name, age = 20, address='서울시 강남구'):
#      print('name = {}, age = {}, address = {}'.format(name, age, address))

# printInfo('한지민', 24, '경기도 수원시')
# printInfo('한지민')
# printInfo('한지민', 34)
# # 기본인자를 사용하는 언어는 오버로딩이 안된다. 오버로딩은 메서드 이름이 같고 파라미터가 달라야 하는데, 파라미터가 정해지지 않아서


#Variable-Length Argument

# def myprint(*args): 
#     for num in args:
#         print(num, end ='\t')
#     print()

# myprint(True)
# myprint((6, 7, 8), [1, 2, 3, 4], 5, 89.5)
# myprint(3, 3, 4, False)

# 아래처럼 변수를 두면 안된다.(가변인자가 중간에 있거나 왼쪽에 있으면 안된다) 왜냐하면 어디까지가 args인지를 모르기 때문에. 
# 항상 가변인자는 오른쪽에 둬야 한다.
# def myprint(*args, su): 
#     for num in args:
#         print(num, end ='\t')
#     print()

# myprint(True)
# myprint((6, 7, 8), [1, 2, 3, 4], 5, 89.5)
# myprint(3, 3, 4, False)


# keyword variable-length argument
# key-value 가 dictionary인데, key-value 쌍의 갯수 가변, keyword도 가변
# def myprint(**args):
#     print('start =' + str(['start']))
#     print('stop =' + str(['stop']))
#     print('step =' + str(['step']))

# myprint(start = 1, stop = 10, step = 2)

# def printInfo(**args):
#     print(args.key())

# printInfo(이름 = '한지민', 나이 = 24)
# printInfo(국어 = 100, 영어 = 90, 수학 = 78)
# printInfo(키 = 184.7, 몸무게=68.2)

# def printInfo(hakbun, name, *subjects, **args):
#     print('hakbun = {}, name = {}'.format(hakbun, name))
#     sum = 0
#     for n in subjects:
#         sum += n
#     print("총점 = {}".format(sum))
#     for (k, v) in args.items():
#         print(k, v)

# printInfo('2020-02', '김지민', 100, 78, language = ('Java', 'Python'), gender='female')
# printInfo('2020-02', '김지민', 100, 78, 56, hobby = ['낚시', '등산', '여행'])

# def add(a, b):  return a+b

# def subtract(a, b):  return a-b

# def multiply(a, b):  return a*b

# def divide(a, b):  return a/b

# aaa = lambda a, b : a + b
# print(aaa(5, 9))
# aaa = lambda a, b : a * b
# print(aaa(5, 9))



# enumerate function 쓰지 않을 때
# scores = [89, 99, 78, 65, 100]
# su = 1
# for num in scores:
#     print(str(su) + '번째 학생의 성적 : ' + str(num))
#     su = su + 1
#또는
# scores = [89, 99, 78, 65, 100]
# for num in range(len(scores)):
#     print(str(num+1)) + '번쨰 학생의 성적 : ' + str(scores[num]))

#enumerate function
# scores = [89, 99, 78, 65, 100]
# for (k, v) in enumerate(scores) :
    # print(str(k+1) + '번째 학생의 성적 : ' + str(v))

# for (k, v) in enumerate(scores, 1) :
#     print(str(k+1) + '번째 학생의 성적 : ' + str(v))


#filter function
# def flunk(score):  #내가 만든 함수
#     return score < 60

# scores = [89, 39, 78, 64, 100]

# for num in filter(flunk, scores): #scores의 내용들이 하나씩 다 flunk에 다녀온다.
#     print(num)

#그런데 만약 lambba를 쓰면 그 함수도 안 만들어된다.

def flunk(score):
      return score < 60

scores = [89, 39, 78, 64, 100]

for num in filter(lambda s : s<60, scores):
    print(num)
    
