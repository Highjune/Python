# import os

# #Current Working Directory
# print('Current Working Directory = ', os.getcwd())

# #PID(Process ID)
# print('Current PID = ', os.getpid())

# #chdir()
# os.chdir(r'C:\temp1')
# print(os.getcwd())

# # with open('서시.txt', 'wt', encoding = 'utf-8') as ptr:
# #     ptr.write('Hello, World')
# #print(dir(os.path))

# import os.path
# print(os.path.isdir('.'))
# print(os.listdir('.'))


# import sys
# print(sys.version)
# print(sys.version_info)
# sys.exit(-1)

# print(sys.argv)

# import os
# #print(os.getcwd())
# os.chdir('../')
# #print(os.getcwd())   #D:\PythonHome
# print(os.listdir('.'))

import shutil
shutil.copy('images/jimin.jpg', 'images/jimin2.jpg')