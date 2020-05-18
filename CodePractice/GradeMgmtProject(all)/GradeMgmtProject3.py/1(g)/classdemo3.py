from student import Student

if __name__ == '__main__' : 
    chulsu = Student('김철수', 24, '서울', '남성')
    print(chulsu)
    chulsu.city = '대전'   #setter
    chulsu.age = 34       #setter

    print(chulsu.name)   #getter
    print(chulsu.gender)  #getter
    print(chulsu)


    # jimin = Student('한지민', 22, '부산', '여성')
    # print(jimin)
