try:
    ptr = open(r'C:\temp1\result.txt', 'r') 
except FileNotFoundError:
    print('File Not Found')
else :
    data = ptr.read()
    print(data)
finally :
    ptr.close()