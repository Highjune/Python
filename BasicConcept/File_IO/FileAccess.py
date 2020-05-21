#tell() : pointer의 현재 위치
#seek() : 특정 위치로 이동

with open('서시.txt', 'r') as ptr:
    ptr.seek(15, 0) #앞에서부터 15번째까지 이동
    print(ptr.tell())


