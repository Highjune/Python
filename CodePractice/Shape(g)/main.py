from square import *
from triangle import *
from circle import *

if __name__ == '__main__' :
    mylist = []
    mylist.append(Square('사각형', 200, 300))
    mylist.append(Triangle('삼각형', 100, 50))
    mylist.append(Circle('원', 150))
    for myshape in mylist:
        myshape.calcArea()
        print(myshape, end = '')
        print(myshape.area, ' 입니다.')