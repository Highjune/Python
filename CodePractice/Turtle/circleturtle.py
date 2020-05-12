import turtle as t

t.shape("turtle")
num = int(input('num : '))
go = int((num-1)/2)
for i in range(1,num):
    for j in range(1,i):
        t.forward(1)
    t.right(90)
