a = 0xABCD
b = 0o21
c = 0b1001010
print(a) #무조건 10진수로 표현됨
print(hex(a)) #함수 이용
print('{0:#x}'.format(a))
print('{0:#o}'.format(a))
print('{0:#b}'.format(a))