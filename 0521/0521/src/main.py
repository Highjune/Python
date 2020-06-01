# class Mammal:
#     def __init__(self):
#         self._name = "Dog"
# 
# class Birds :
#     def __init__(self):
#         self._name = "Sparrow"
#         
# class Bat(Birds,Mammal):
#     @property
#     def name(self): return self._name
#     
# bat = Bat()
# print(bat.name)
# print(Mammal()._name)
# print(Birds()._name)
# bat._name = 'Cat'
# print(bat.name)
#print(dir(bat))
#print(bat.__class__.__name__)
#print(dir(Mammal))

kor = 102
assert 0 <= kor <= 100,  "국어 점수가 잘 못 처리됐습니다."
print('kor = ', kor)




