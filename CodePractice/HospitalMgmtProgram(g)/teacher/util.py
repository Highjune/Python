#util.py
def getDepartment(code):
    if code == 'MI': return '외과'
    elif code == 'NI': return '내과'
    elif code == 'SI': return '피부과'
    elif code == 'TI': return '소아과'
    elif code == 'VI': return '산부인과'
    elif code == 'WI': return '비뇨기과'
    
def getOpFee(age):
    if age < 10 : return 7000
    elif 10 <= age < 20 : return 5000
    elif 20 <= age < 30 : return 8000
    elif 30 <= age < 40 : return 7000
    elif 40 <= age < 50 : return 4500
    elif age > 50 : return 2300
    
def getDiscount(days):
    if days < 10 : return 1.0
    elif 10 <= days < 15 : return 0.85
    elif 15 <= days < 20 : return 0.8
    elif 20 <= days < 30 : return 0.77
    elif 30 <= days < 100 : return 0.72
    elif 100 <= days : return 0.68
    
def getGoinPrice(days):
    if days <= 3 : return 30000
    else : return 25000
    