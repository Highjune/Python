import xml.etree.ElementTree as ET
from student import Student

def myinput(mylist):
    try:
        xml_ = ET.parse('sungjuk_utf8.xml')   #ElementTree
        root = xml_.getroot()    #Element
        #print(root.tag)     #students
        students = list(root)
        for student in students :
            hakbun = student.attrib['hakbun']
            irum = student.find('irum').text.strip()
            kor = int(student.find('kor').text.strip())
            eng = int(student.find('eng').text.strip())
            mat = int(student.find('mat').text.strip())
            edp = int(student.find('edp').text.strip())
            mylist.append(Student(hakbun, irum, kor, eng, mat, edp))
    except :
        print('Exception')