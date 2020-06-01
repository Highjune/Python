#main3.py

# try:
#     ptr = open(r'C:\temp1\result.dat', 'w')
#     ptr.write("""한 점 부끄럼이 없기를
# 잎새에 이는 바람에도
# 나는 괴로와 했다.""")
# except:
#     print('Exception 발생')
# else : 
#     print('Save Successfully')
# finally : 
# #     ptr.close()
# 
# try:
#     ptr = open(r'C:\temp1\result.dat', 'r')
# except FileNotFoundError : 
#     print('File Not Found')
# else :
#     data = ptr.read()
#     print(data)
# finally:
#     ptr.close()
    

try:
    ptr = open('main3.py', 'r', encoding='utf-8')
except:
    print('File Not Found')
else :
    line = ptr.readline()
    while line :
        print(line, end = '')
        line = ptr.readline()
finally:
    ptr.close()






