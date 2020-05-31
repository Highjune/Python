from util import *

def mycalc(mylist):
    for n in range(len(mylist)):
        patient = mylist[n]
        totalGoin = getGoinPrice(patient.days) * patient.days  #총입원비
        goin = int(totalGoin * getDiscount(patient.days))     #입원비
        money = getOpFee(patient.age) + goin   #진료비
        patient.department = getDepartment(patient.code)  #진료부서
        patient.fee = getOpFee(patient.age)  #진찰비
        patient.goin = goin   #입원비
        patient.money = money