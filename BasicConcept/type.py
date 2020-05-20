
name = '한지민'
age = int(input('나이 : '))
print('Name : %s, Age = %d' %(name, age))

#파이썬은 자동형변환이 되지 않기 때문에 input으로 받은 것은 무조건 string이므로 %d(10진수)로 받게 되면 에러난다.
#그래서 int로 형변환해야지 오류가 나지 않는다.