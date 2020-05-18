#telephone.py
class Telephone :
    """
        Object : 전화요금 관리프로그램을 위한 Telephone Class
        Author : June
        When : 2020-05-18
        Environment : Windows 10. VSCode. Python 3.8.2   
    """
    def __init__(self, str): #'한지민    25  1   010-2345-4567'
        self._name = str.split('\t')[0]
        self._tongwha = str.split('\t')[1]
        self._tel = str.split('\t')[2]

    def __str__(self):
        return '{}\t\t{}\t\t{}'.format(self._name, self._tongwha, self._tel)
       
# mytelephone = Telephone()
# print(mytelephone.__doc__)
