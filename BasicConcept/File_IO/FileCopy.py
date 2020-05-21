#file copy

# with open(r'C:/target.png', 'wb') as ptr :
#     print(ptr.writable())
    #안되서 Permission denied 뜸
    
    
original = input('복사할 파일명 : ')
target = input('복사한 파일명: ')
mode = True
buffersize = 100
if original.endswith('.png') or original.endswith('.jpg') or original.endswith('.gif'):
    mode = False
    
try :
    ptr1 = ptr2 = None
    if mode : 
        ptr1 = open(original, 'rt', encoding = 'utf-8')
        ptr2 = open(target, 'wt', encoding = 'utf-8')
    else : 
        ptr1 = open(original, 'rb')
        ptr2 = open(original, 'wb')
    
    readdata = ptr1.read(buffersize)
    while readdata : 
        ptr2.write(readdata)
        readdata = ptr1.read(buffersize)            
except Exception as ex :
    print("Exception 발생", ex.args)
else :
    print('Copied Successful')        
finally :
    ptr1.close()
    ptr2.close()
    
    
    
