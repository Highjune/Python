#calc
#번호 진료코드 입원일수 나이
#번호 진찰부서 진찰비 입원비 진료비
# 번호-num# 진료코드-code# 입원일수-ibwonilsu# 나이-age# 진찰부서-jindept# 진찰비-jinchalfee# 입원비-ibwonfee# 총 입원비-totalibwon# 진료비-jinryofee

from process import getjindept
from process import getjinchalfee
from process import getsale

def mycalc(mylist):
    for n in range(len(mylist)):
        h = mylist[n]
        #####
        num=0
        jindept=getjindept(h.code)
#         code = 0 ###jindept
        onedaypay = 0 # 하루 입원비
        sale = getsale(h.ibwonilsu) # 할인율 ###
        jinchalfee = getjinchalfee(h.age) # 진찰비###
        #####
        if h.ibwonilsu <= 3 : onedaypay = 30000
        else : onedaypay = 25000
        
        totalibwon = onedaypay * h.ibwonilsu # 총입원비
        
        ibwonfee = totalibwon * sale # 입원비
        
        jinryofee = jinchalfee + ibwonfee #진료비
    
        h.jindept = jindept
        h.jinchalfee = jinchalfee
        h.ibwonfee = ibwonfee
        h.jinryofee = jinryofee
        

