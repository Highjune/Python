#1. 
# while (True):
#     su = int(input('양의 정수를 입력하세요 : '))
#     if (su > 0):
#         if su % 2 == 0 :
#             print('짝수입니다.')
#             break
#         else : 
#             print('홀수입니다.')
#             break
#     else :
#         print('반드시 양의 정수를 입력하셔야 합니다.')


#2. 
# sum = 0
# for num in range(1, 51):
#     if num % 3 == 0 :
#         sum += num
#     else :
#         pass

# print('sum = %d' % sum)

#3. 
# for i in range(0, 5):
#     for j in range(0, 5):
#         print('*', end = '')
#     print()

#4. 
# for i in range(0, 5):
#     for j in range(0, i + 1):
#         print('*', end = '')
#     print()

#5. 
# for i in range(0, 5):
#     for j in range(i, 5):
#         print('*', end = '')
#     print()

#6. 
for i in range(0, 5):
    for j in range(i+1, 5):
        print(' ', end = '')  #공백출력
    for k in range(i*2+1): 
        print('*', end = '')
    print()



###################################
#numbers = [1,2,3,4,5,6,7,8,9,10]
#1
#numbers.append(100)
#print(numbers)
#2
#data = [200,300,400,500]
#numbers.extend(data)
#print(numbers)

#3.
# numbers = [1,2,3,4,5,6,7,8,9,10]
#print(numbers[:5])

#4. 
#print(numbers[1::2])

#5.
#numbers[1::2] = [0,0,0,0,0] 
#numbers[1::2] = [0] * 5
#numbers[1::2] = [0] * int(len(numbers) / 2)
#print(numbers)

#6. 
#print(numbers[::-1])

#7.
# member_info = {'name' : '한지민', 'age' : 24, 'address' : '서울시 강남구', 'score' : 90}
#print(member_info['address'])

#8. 
#print(member_info.pop('score'))

#9. 
#member_info['address'] = '경기도 수원시'
#print(member_info)
# mylist = list(member_info.values())
# print(mylist)