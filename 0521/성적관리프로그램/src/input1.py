#input1.py
from student import Student
 
def myinput(mylist):
    with open('../sungjuk_utf8.dat', 'rt', encoding = 'utf-8') as ptr:
        try:
            while True:
                line = ptr.readline()   #1101     한송이     78     87     83     78
                if not len(line) : break
                array = line.strip().split()
                student = Student(array[0], array[1], int(array[2].strip()), 
                            int(array[3].strip()), int(array[4].strip()), int(array[5].strip()))
                mylist.append(student)
        except FileNotFoundError :
            print("File Not Found")
        except Exception as ex:
            print('Exception = ', type(ex))