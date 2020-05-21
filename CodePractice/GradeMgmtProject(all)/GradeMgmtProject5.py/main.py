from input1 import myinput
from output1 import myoutput
from calc import mycalc
from sort1 import selectionSort

if __name__ == '__main__':
    mylist = []
    myinput(mylist)
    mycalc(mylist)
    selectionSort(mylist)
    myoutput(mylist)