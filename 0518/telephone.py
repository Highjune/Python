#telephone.py
class Telephone : 
    """
        Object : 전화요금 관리프로그램을 위한 Telephone Class
        Author : Instructor
        When : 2020-05-18
        Environment : Windows 10, VSCode, Python 3.8.2    
    """
    def __init__(self, str):  # '한지민    25      010-2345-6789'
        self._name = str.split(',')[0]
        self._tongwha = str.split(',')[1]
        self._tel = str.split(',')[2]

    def __str__(self):
        return '{}\t\t{}\t\t{}'.format(self._name, self._tongwha, self._tel)

# mytelephone = Telephone()
# print(mytelephone.__doc__)