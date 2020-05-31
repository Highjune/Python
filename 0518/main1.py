#main1.py
# import mypack.calc.add
# import mypack.calc.multi
# import mypack.report.myreport
# from mypack.calc.add import myadd as add
# from mypack.calc.multi import mymulti as multi
# from mypack.report.myreport import report as mr

from mypack.calc import *
from mypack.report import *
# from mypack.report.myreport import report as rp

if __name__ == '__main__':
    add.myadd(5, 9)
    multi.mymulti(5, 9)
    myreport.report()
