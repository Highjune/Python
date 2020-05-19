#calc.py

def mycalc(mylist):
    for n in range(len(mylist)):
        student = mylist[n]
        total = student.kor + student.eng + student.mat
        avg = round(total / 3, 2)
        grade = None
        if avg >= 90 : grade = 'A'
        elif avg >=80 : grade = 'B'
        elif avg >=70 : grade = 'C'
        elif avg >=60 : grade = 'D'
        else : grade = 'F'
        
        student.total = total
        student.avg = avg
        student.grade = grade    
    