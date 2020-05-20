#readfileself.py

try :
    ptr = open('C:/temp1/result.txt', 'w')  #write
#     ptr = open('C:\\temp1\\result.txt', 'w') 
#     ptr = open(r'C:\temp1\result.txt', 'w')

    #'w'로 할 경우 기존의 내용을 덮는다
    ptr.write("""죽는 날까지 하늘을 
    우러러)
    나는 괴로워 했다""")
except :
    print('Exception 발생')
else :
    print("Save SuccessFully")
finally :
    ptr.close()
    
    