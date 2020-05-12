#1~100합
sum = 0
for i in range(1, 100):
	sum += i
	print('sum = ' + str(sum))

#구구단 7단
for i in range(1, 10):
    	print('7 x' + str(i) + ' = ' + str(7*i))

#구구단
for i in range(1, 10) :
    for j in range(2, 10) :
        print(str(j) + ' x ' + str(i) + ' = ' + str(j*i), end = '\t')
    print()
