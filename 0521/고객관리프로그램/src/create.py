#create.py
import gradecheckerror 
import customer
def create_customer():
    name = input('이름 : ')
    tel = input('전화번호 : ')
    email = input('이메일 : ')
    age = int(input('나이 : '))
    grade = None
    while True : 
        grade = int(input('고객등급(1 ~ 5) : '))
        if 1 <= grade <= 5 : break
        else : 
            #raise gradecheckerror.GradeCheckError()
            print('고객 등급은 1 ~ 5등급만 유효합니다.')
            continue
    etc = input('기타정보 : ')
    mycustomer = customer.Customer(name, tel, age, grade, email, etc)
    return mycustomer