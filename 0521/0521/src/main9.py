#tell() : pointer의 현재 위치
#seek() : pointer를 특정 위치로 이동
with open('서시1.txt', 'r', encoding='utf-8') as ptr:
    ptr.seek(20)  #앞에서부터 15번째까지 이동
    print(ptr.read())
    print(ptr.tell())