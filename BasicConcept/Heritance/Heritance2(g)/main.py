import person, student, employee

if __name__ == '__main__':
    chulsu = student.Student('김철수', 24, '2020-01')
    younghee = employee.Employee('이영희', 25, 'sist2020-1', 3000)
    print(chulsu)
    print(younghee)
    chulsu.workhard()
    younghee.workhard()