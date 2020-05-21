#나를 읽는 것

try:
    ptr = open('readfileself.py', 'r', encoding='utf-8') 
except:
    print('File Not Found')
else :
    line = ptr.readline()
    while line :
        print(line, end = '')
        line = ptr.readline()
finally :
    ptr.close()
    