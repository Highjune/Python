def myinput():
    for n in range(3):
        student = {}
        student['name'] = input('이름 : ')
        student['kor'] = int(input("국어 : "))
        student['eng'] = int(input("영어 : "))
        student['mat'] = int(input("수학 : "))
        students.append(student)
    return None

def mycalc():
    for n in range(len(students)):
        total = students[n]['kor'] + students[n]['eng'] + students[n]['mat']
        avg = round(total / 3, 2)
        grade = getGrade(avg)
        students[n]['total'] = total;  students[n]['avg'] = avg; students[n]['grade'] = grade

def getGrade(avg):
    if avg >= 90 : return 'A'
    elif avg >= 80 : return 'B'
    elif avg >= 70 : return 'C'
    elif avg >= 60 : return 'D'
    else : return 'F' 

def mysort():
    students.sort(key = lambda s : s['total'], reverse = True)

def myoutput():
    for n in range(len(students)):
        std = students[n]
        print('{} {} {} {} {} {} {}'
            .format(std['name'], std['kor'], std['eng'], std['mat'], std['total'],
            std['avg'], std['grade']))

students = []
myinput()
mycalc()
mysort()
myoutput()