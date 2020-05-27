from student import Student
import json

def myoutput2(mylist):
    with open('result.json', 'wt', encoding='utf-8', newline='') as ptr:
        try:
            for student in mylist:
                obj = student.convertDict()
                json.dump(obj, ptr, ensure_ascii=False, indent='\t')
        except : 
            print('JSON Exception')
        else :
            print('Save successfully')