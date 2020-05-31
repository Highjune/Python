#output.py

def printLabel():
    print('<<병원관리프로그램>>'.center(60))
    print('-' * 60)
    print('번호\t진찰부서\t진찰비\t\t입원비\t\t진료비')
    print('-' * 60)
    
def myoutput(mylist):
    printLabel()
    for n in range(len(mylist)):
        print(mylist[n])