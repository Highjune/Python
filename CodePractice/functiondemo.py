# def calc(start, stop):
#     sum = 0 
#     for num in range(start, stop+1):
#         sum += num
#     #print('sum = ' + str(sum))
#     return sum


# # calc(); #Call by Name
# print(calc(1,100)); #Call by Value
# print(calc(1,10));


# def change(su):
#     print(id(su))
# a=5
# change(5)
# print('Function out : ' + str(id(a)))
#su와 a의 주소가 같다.
#5가 복사된 것이 아니라 5가 저장되어 있는 주소가 복사


# def change(su):
#     su = 100

# a=5
# change(a)
# print('a = ' + str(a))
#5를 가리키고 있는 a의 주소는 변하지 않는다. 상수는 변하지 않는다. 
#그래서 change()에 다녀오더라도 a는 5를 가리키고 있는 주소 그대로임

def change(su):
    su = [100, 200, 300, 400, 500]

a = [5, 6, 7, 8, 9, 10]
change(a)
print(a)
#list자체는 바뀌지 않는다. 