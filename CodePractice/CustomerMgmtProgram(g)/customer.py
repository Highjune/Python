class Customer(object):
    def __init__(self, name, tel, age, grade, email, etc):
        self._name = name
        self._tel = tel
        self._age = age
        self._grade = grade
        self._email = email
        self._etc = etc

    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}'\
            .format(self._grade, self._name, self._tel, self._email, self._age, self._etc)