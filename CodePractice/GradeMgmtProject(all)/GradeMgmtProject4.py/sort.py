#sort.py

# def getTotal(std):
#     return std.total
def mysort(mylist):
#     mylist.sort(key = getTotal, reverse = True) #key는 함수이름(정렬기준)을 써야하고, reverse가 true면 내림차준. 
    mylist.sort(key = lambda std : std.total, reverse = True)
     
    
    