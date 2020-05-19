from input import myinput
from output import myoutput
from calc import mycalc
from sort import mysort

print(__name__)

if __name__ == '__main__':
    mylist = list()
    myinput(mylist)
    mycalc(mylist)
    mysort(mylist)  
    myoutput(mylist)