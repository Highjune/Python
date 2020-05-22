def update_customer(mycustomer):
    tel = mycustomer.tel
    email = mycustomer.email
    age = mycustomer.age
    grade = mycustomer.grade
    etc = mycustomer.etc
    
    newTel = input('변경할 전화번호 : ')
    if not len(newTel) : #변경하지 않으려고 그냥 enter키를 눌렀다면
        newTel = tel
    newEmail = input('변경할 Email : ')
    if not len(newEmail) : #변경하지 않으려고 그냥 enter키를 눌렀다면
        newEmail = email
    newAge = input('변경할 나이 : ')
    if not len(newAge) : #변경하지 않으려고 그냥 enter키를 눌렀다면
        newAge = age
    else : newAge = int(newAge)  #정수로 변환
    newGrade = input('변경할 고객등급(1 ~ 5) : ')
    if not len(newGrade) : #변경하지 않으려고 그냥 enter키를 눌렀다면
        newGrade = grade
    else : newGrade = int(newGrade)
    newEtc = input('변경할 특징점 : ')
    if not len(newEtc) : #변경하지 않으려고 그냥 enter키를 눌렀다면
        newEtc = etc
        
    mycustomer.age = newAge
    mycustomer.email = newEmail
    mycustomer.etc = newEtc
    mycustomer.grade = newGrade
    mycustomer.tel = newTel
    print('수정완료')