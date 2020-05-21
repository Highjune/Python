#output1.py

def printLabel(ptr):
    ptr.writelines('<<쌍용고등학교 성적표>>'.center(65))
    ptr.writelines('\n')
    ptr.writelines('-' * 65)
    ptr.writelines('\n')
    ptr.writelines('등수\t학번\t이름\t국어\t영어\t수학\t전산\t총점\t평균\t평점\n')
    ptr.writelines('-' * 65)
    ptr.writelines('\n')
    
def myoutput(mylist):
    with open('result.dat', 'at', encoding = 'utf-8') as ptr:
        try:
            printLabel(ptr)
            for n in mylist:
                ptr.writelines(str(n))
                ptr.writelines('\n')
        except Exception as ex: 
            print('Exception = ', type(ex))
        else  :
            print('Save Successfully')