from input import myinput
from output import myoutput
from calc import mycalc
from sort import mysort

if __name__ == '__main__':
#     younghee = myinput()
#     mycalc(younghee)  
#     myoutput(younghee)
    
    mylist = []
    myinput(mylist)
    mycalc(mylist)
    mysort(mylist)
    myoutput(mylist)
    