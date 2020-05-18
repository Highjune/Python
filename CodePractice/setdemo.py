# myset = {1, 5, 3, 6, 1, 2, 7, 2, 1, 5, 3, 7}
# myset1 = {100, 200, 300}
# print(myset + myset1)
# print(myset * 3)

myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
myset1 = {5, 6, 7, 8, 9, 10, 11, 12, 13}
#합집합
print(myset.union(myset1))
print(myset | myset1)

#교집합
print(myset.intersection(myset1))
print(myset & myset1)

#차집합
print(myset.difference(myset1))
print(myset - myset1)