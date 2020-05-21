mylist = [4, 34.1, True, ['apple', 'banana', 'Grape']]



mylist  = list()
for i in range(1, 6):
    mylist.append(input('Enter a fruits: '))
print(mylist)



mylist  = list()
for i in range(1, 6):
    mylist.append(input('Enter a fruits: '))
print(mylist[0])  #0 1 2 3 4
print(mylist[-1]) #-5 -4 -3 -2 -1




mylist = list()
while (str := input('입력 : ')) != 'quit' :
    mylist.append(str)

print(mylist)