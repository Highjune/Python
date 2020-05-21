class Student:
    def __init__(self, hakbun, name, kor, eng, mat, edp):
        self._hakbun = hakbun
        self._name = name
        self._kor = kor
        self._eng = eng
        self._mat = mat
        self._edp = edp
        self._ranking = 1
        
    @property
    def hakbun(self): return self._hakbun
    @property
    def name(self): return self._name
    @property
    def kor(self): return self._kor
    @property
    def eng(self): return self._eng
    @property
    def mat(self): return self._mat
    @property
    def edp(self): return self._edp
    
    @property
    def total(self): return self._total
    @total.setter
    def total(self, total): self._total = total
    
    @property
    def avg(self): return self._avg
    @avg.setter
    def avg(self, avg):  self._avg = avg
    
    @property
    def grade(self): return self._grade
    @grade.setter
    def grade(self, grade): self._grade = grade
    
    @property
    def ranking(self): return self._ranking
    @ranking.setter
    def ranking(self, ranking): self._ranking = ranking
    
    def __str__(self):  #tostring()
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self._ranking, 
                                                               self._hakbun,  self._name,
                                                       self._kor, self._eng, self._mat, self._edp,
                                                       self._total, self._avg, self._grade)
    
    
    
    
    
    
    
     
    
    