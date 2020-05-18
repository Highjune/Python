# 1. 숫자(양의 정수)를 입력받아 홀수인지 짝수인지 판별하는 프로그램 작성하기. 단,
# 양의 정수가 아니면 숫자를 다시 입력받아야 한다.

# while(True):
#     su = int(input('양의 정수를 입력하세요 : '))
#     if (su > 0) :
#         if su % 2 == 0 :
#             print('짝수입니다.')
#             break
#         else :
#             print('홀수입니다.')
#             break
#     else :
#         print('양의 정수를 입력하셔야 합니다. ')


# 2. 1부터 50까지 자연수 중에서 3의 배수의 총합을 출력하는 프로그램 작성하기
# sum = 0
# for num in range(1, 51) :
#     if num % 3 == 0 :
#         sum += num
#     else :
#         pass
# print('sum = %d ' % sum)

# 3. 아래와 같은 패턴의 별(*)들을 출력하는 프로그램 작성하기
# *****
# *****
# *****
# *****
# *****

# for i in range(0, 5) :
#     for j in range(0, 5) :
#         print('*', end = ' ')
#     print()


# 4. 아래와 같은 패턴의 별(*)들을 출력하는 프로그램 작성하기
# *
# **
# ***
# ****
# *****

# for i in range(0, 5):
#     for j in range(0, i+1):
#         print('*', end = ' ')
#     print()

# 5. 아래와 같은 패턴의 별(*)들을 출력하는 프로그램 작성하기
# *****
# ****
# ***
# **
# *    

# for i in range(0, 5):
#     for j in range(i, 5):
#         print('*', end = '')
#     print()


# 6. 아래와 같은 패턴의 별(*)들을 출력하는 프로그램 작성하기
#     *
#    **
#   ***
#  ****
# *****

# for i in range(0, 5):
#     for j in range(i+1, 5): 
#         print(' ' , end='') #공백출력
#     for k in range(i+1): 
#         print('*', end='')
#     print()


# 7. 아래와 같은 패턴의 별(*)들을 출력하는 프로그램 작성하기
# *****
#  ****
#   ***
#    **
#     *

# for i in range(0, 5):
#     for k in range(i, 5): 
#         print('*', end='')    
#     for j in range(i+1): 
#         print(' ' , end='') 
#     print()


#8 아래와 같은 패턴의 별(*)들을 출력하는 프로그램 작성하기
#     *
#    ***
#   *****
#  *******
# *********
# for i in range(0, 5):
#     for j in range(i+1, 5): 
#         print(' ' , end='') #공백출력
#     for k in range(i*2+1): 
#         print('*', end='')
#     print()

########################################################################################################################################
#list문제
#다음 list가 주어졌을 경우 요구사항대로 코드 작성
# numbers = [1,2,3,4,5,6,7,8,9,10]
#1. 숫자 100을 제일 뒤에 추가하기
# numbers.append(100)
# print(numbers)


#2. 다음 list를 numbers 리스트 제일 뒤에 추가하기
# numbers = [1,2,3,4,5,6,7,8,9,10]
# data = [200, 300, 400, 500]
# numbers.extend(data)
# print(numbers)


#3. 처음 다섯 개 숫자만 출력하기
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[0:5]) 
# print(numbers[:5]) #생략하면 0이다
# slicing


#4. list에서 짝수 번째(인간기준 : 1부터 시작) 데이터만 출력하기
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[1::2]) #1부터 끝(생략)까지 2칸씩 증가



#5. 짝수 번째(인간기준) 데이터를 모두 0으로 바꾸기
# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers[1::2] = [0, 0, 0, 0, 0]
# numbers[1::2] = [0] * 5       #이렇게 해도 됨
# numbers[1::2] = [0] * int(len(numbers)/2)       #이렇게 해도 됨
# print(numbers)



#6. 데이터를 역순으로 나열하기(내림차순 정렬이 아님)
#print(numbers[::-1])

#############################################################################################################################################
#dictionary
# 다음 dictionary 데이터가 주어졌을 때 요구사항대로 코드 작성하기
# member_info = {'name' : '한지민', 'age' : 24,'address' : '서울시 강남구', 'score' : 90}
# 7.address 값 출력하기
# print(member_info['address'])

# 8.score를 출력하고 member_info 딕셔너리에서 삭제하기
# member_info = {'name' : '한지민', 'age' : 24,'address' : '서울시 강남구', 'score' : 90}
# print(member_info.pop('score'))

# # 9. address를 '경기도 수원시'로 변경하기
# member_info = {'name' : '한지민', 'age' : 24,'address' : '서울시 강남구', 'score' : 90}
# member_info['address'] = '경기도 수원시'
# print(member_info)

# 9. member_info 딕셔너리 데이터의 값을 list로 출력하기
# member_info = {'name' : '한지민', 'age' : 24,'address' : '서울시 강남구', 'score' : 90}
# mylist = list(member_info.values())
# print(mylist)
