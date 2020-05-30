# def calc(start, stop):
#     sum = 0
#     for num in range(start, stop + 1):
#         sum += num
#     #print('sum = ' + str(sum))
#     return None

# #calc()   #Call by Name
# print(calc(1,100))    #Call by Value
# print(calc(1,10))

def change(su):   #Call by Reference
    su= [100, 200, 300, 400,500]
    #print('Function in : ' + str(id(su)))

a = [5, 6,7,8,9,10]
change(a)
print(a)
#print('Function out : ' + str(id(a)))

#Python에서의 Call by Value와 Call By Reference의 차이점
#1. Python에서는 모든 변수는 상수다.
#2. Python은  모두 Call By Reference다.
#3. 그럼에도 불구하고, 주소를 넘기면 값은 변경되지 않는다.
#4. 다만, list나 dict를 넘기면 그 멤버의 값은 변경할 수 있다.