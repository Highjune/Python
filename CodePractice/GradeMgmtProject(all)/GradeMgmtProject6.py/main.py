from input import myinput
from output import myoutput
from output1 import myoutput1
from output2 import myoutput2
from calc import mycalc

if __name__ == '__main__':
    mylist = []
    myinput(mylist)
    mycalc(mylist)
    myoutput(mylist)   #Standard Output
    myoutput1(mylist)  #Sqlite3 Output
    myoutput2(mylist)   #JSON Output

