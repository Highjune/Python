class Customer(object):
    def __init__(self, name, tel, age, grade, email, etc):
        self._name = name
        self._tel = tel
        self._age = age
        self._grade = grade
        self._email = email
        self._etc = etc

    @property
    def name(self): return self._name
    @property
    def tel(self): return self._tel
    @tel.setter
    def tel(self, newTel): self._tel = newTel
    @property
    def age(self): return self._age
    @age.setter
    def age(self, newAge): self._age = newAge
    @property
    def grade(self): return self._grade
    @grade.setter
    def grade(self, newGrade): self._grade = newGrade
    @property
    def email(self): return self._email
    @email.setter
    def email(self, newEmail): self._email = newEmail
    @property
    def etc(self): return self._etc
    @etc.setter
    def etc(self, newEtc): self._etc = newEtc
    
    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}'\
            .format(self._grade, self._name, self._tel, self._email, self._age, self._etc)
            
    def getInfo(self):    
        return [self._name, self._tel, self._age, self._grade, self._email, self._etc]