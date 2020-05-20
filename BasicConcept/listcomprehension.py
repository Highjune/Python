# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# myotherlist = []



# for i in mylist:
#     myotherlist.append(i)
# print(myotherlist)



# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# myotherlist = [i for i in mylist]
# print(myotherlist)



# print([n ** 2 for n in range(1, 11)])

#조건문추가
# print([n ** 2 for n in range(1, 11) if n ** 2 > 30])

#mylist에서 정수만 뽑아내기
# mylist = [56, 3.14, True, [1, 2, 3], (4, 5, 6), {'name':'Sonata'}, 67, 89.5]
# print([n for n in mylist if type(n) == int])


#else가 없는 if
# mylist = [34, -36, 12, -6, 9, 3, -5, -2]
# print([for n in mylist if n > 0])

#else가 있는 if
# mylist = [34, -36, 12, -6, 9, 3, -5, -2]
# print([n if n>0 else 0 for n in mylist])

#2차원 list
# mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([n for row in mylist for n in row])







