# import os

#Current Working Directory
# print('Current Working Directory = ', os.getcwd()) 
#PID(Process ID)
# print('Current PID = ', os.getpid())

#chdir()
# os.chdir(r'C:\temp1')
# print(os.getcwd())

# with open('서시.txt', 'wt', encoding = 'utf-8') as ptr:
#     ptr.write('Hello, World')

# print(os.path)
# print(dir(os.path))


# import os.path
# print(os.path.isdir('.'))
# print(os.listidr('.'))

# import sys
# print(sys.version)
# print(sys.version_info)
# sys.exit(0) #프로그램 종료, 0이면 정상종료, -1이면 비정상종료

# print(sys.argv)

import os
print(os.getcwd())
os.chdir(r'D:\PythonHome\0521')
print(os.getcwd()) #D:\pythonHome
print(os.listdir('.'))

import shutil
shutil.copy('images/messi.jpg', 'images/messi2.jpg')

    