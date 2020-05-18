name = input('Name : ')
age = int(input('Age : '))
kor = int(input('kor : '))
eng = int(input('eng : '))
mat = int(input('mat : '))
sum = kor + eng + mat
avg = sum / 3
grade = None
if 90 <= avg <= 100 :  grade = 'A'
elif 80 <= avg < 90 :  grade = 'B'
elif 70 <= avg < 80 :  grade = 'C'
elif 60 <= avg < 70 :  grade = 'D'
else : grade = 'F'
print('이름 = {0}, 나이 = {1}'.format(name, age))
print('국어 = {0}, 영어 = {1}, 수학 = {2}, 총점 = {3}, 평균{4}, 평점 = {5}'.format(kor, eng, mat, sum, avg, grade))