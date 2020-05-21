import os, sys

def list(mypath):
    mylist = os.listdir(mypath)
    for my in mylist:
        newPath = os.path.join(mypath, my)
        # print(newPath)
        print(os.path.abspath(my))

if __name__ == '__main__' :
    path = sys.argv[1] #$ python main1.py D:\PythonHome
    list(path)
