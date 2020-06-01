class Member:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __str__(self):
        return 'Name = {}\tAge={}'.format(self._name, self._age)
# 
# mylist = []
# mylist.append(Member('한지민', 24))
# mylist.append(Member('박지민', 34))
# mylist.append(Member('김지민', 44))

import pickle

with open('C:/temp1/members.pkl', 'rb') as ptr:
    mylist = pickle.load(ptr)
    for member in mylist:
        print(member)
# with open('C:/temp1/members.pkl', 'wb') as ptr:
#     pickle.dump(mylist, ptr)
#     print('Save Successfully')

