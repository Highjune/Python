
class Student:
    def __init__(self, hakbun, name, kor, eng, mat):
        self._hakbun=hakbun
        self._name = name
        self._kor = kor
        self._eng = eng
        self._mat = mat
        
    @property  #getter
    def hakbun(self): return self._hakbun 
    
    @property  #getter
    def name(self): return self._name 
    
    @property  #getter
    def kor(self): return self._kor 
    
    @property  #getter
    def eng(self): return self._eng 
    
    @property  #getter
    def mat(self): return self._mat 
    
    @property
    def total(self): return self._total
    
    @total.setter #변수명.setter ==> setter
    def total(self, total): self._total = total
    
    @property
    def avg(self): return self._avg
    
    @avg.setter
    def avg(self, avg): self._avg = avg
    
    @property
    def grade(self): return self._grade
    
    @grade.setter
    def grade(self, grade): self._grade = grade
    
    def __str__(self): #toString()
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self._hakbun, self._name, 
                                            self._kor, self._eng, self._mat, self._total, self._avg, self._grade)
    
    
    
    