#car = { 'name' : 'Sonata', 'price':25000000, 'maker':'Hyundai'}
# print(type(car))   #<class 'dict'>
# print(car['name'])
# print(car['price'])
# car['price'] = 30000000   #update
# print(car['price'])
# car['bgcolor'] = 'Silver'
# print(car)
#print(car.name)

#car = { 'name' : 'Sonata', 'price':25000000, 'maker':'Hyundai'}
# del car['maker']   #maker 라는 key제거
# print(car)
# car.clear()
# print(car)
# del car
# print(car)

# car = { 'name' : 'Sonata', 'price':25000000, 'maker':'Hyundai'}
# keys = car.keys()
# print(type(keys))
# print(keys)
# values = car.values()
# print(values)
# items = car.items()
# print(items)

students = []
for n in range(3):
    student = {}
    student['name'] = input('Name : ')
    student['age'] = int(input('Age : '))
    student['address'] = input('Address : ')
    students.append(student)

print(students)