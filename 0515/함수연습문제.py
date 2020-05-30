#1. 
# def get_max_min(data_list):
#     #return [max(data_list), min(data_list)]
#     # data_list.sort()
#     # return [data_list[0], data_list[len(data_list) - 1]]
#     max = data_list[0]
#     min = data_list[0]
#     for n in data_list:
#         if max < n : max = n
#         if min > n : min = n

#     return min, max

# print(get_max_min([1,6,2,3,9,4]))


#2. 
# def getBmi(weight, height):
#     result = None
#     bmi = round(weight / height ** 2 * 10000, 1)
#     if bmi < 18.5 : result  = '마른체형' 
#     elif 18.5 <= bmi < 25.0 : result = '표준'
#     elif 25.0 <= bmi < 30.0 : result = '비만'
#     elif bmi >= 30.0 : result = '고도비만'
#     return weight, height, bmi, result

# print(getBmi(72.8, 179.2))

#3. 
import math
def get_triangle(width, height):
    area = width * height / 2
    perimeter = width + height + math.sqrt(width ** 2 + height ** 2)
    return area, perimeter

#4. 
def mysum(from,end):
    sum = 0
    for n in range(from, end + 1):
        sum += n
    return sum

#5. 
def get_abbrs(list):
    for n in range(len(list)):
        return list[n][:3]


#6. 
def isPrime(su):
    for n in range(2, su):
        if su % n == 0 : return False
    return True

#7.
def printPrime():
    count = 0
    mylist = []
    start = 2
    while True:
        for n in range(2, 10000):
            if isPrime(n) : 
                mylist.append(n)
                count = count + 1
                if count > 29 : break
    return mylist