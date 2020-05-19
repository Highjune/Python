#process


def getjindept(code):
    jindept = None
    if code == "MI":
        jindept = "외과"
    elif code == "NI":
        jindept = "내과"
    elif code == "SI":
        jindept = "피부과"
    elif code == "TI":
        jindept = "소아과"
    elif code == "VI":
        jindept = "산부인과"
    elif code == "WI":
        jindept = "비뇨기과"
    else : "???"
    return jindept


def getjinchalfee(age):
    jinchalfee = None
    if age >= 50 :
        jinchalfee=2300
    elif age >= 40:
        jinchalfee=4500
    elif age >= 30:
        jinchalfee=7000
    elif age >= 20:
        jinchalfee=8000
    elif age >= 10:
        jinchalfee=5000
    else :
        jinchalfee=7000
    return jinchalfee

def getsale(ibwonilsu):
    sale = None
    if ibwonilsu >= 100 : 
        sale = 0.68
    elif ibwonilsu >= 30:
        sale = 0.72
    elif ibwonilsu >= 20:
        sale = 0.77
    elif ibwonilsu >= 15:
        sale = 0.80
    elif ibwonilsu >= 10:
        sale = 0.85
    else :
        sale = 1.00   
    return sale
    

