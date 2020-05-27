class Student:
    def __init__(self, hakbun, irum, kor, eng, mat, edp):
        self._hakbun = hakbun
        self._irum = irum
        self._kor = kor
        self._eng = eng
        self._mat = mat
        self._edp = edp
        
    @property
    def hakbun(self): return self._hakbun
    @property
    def irum(self): return self._irum
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
    
    def __str__(self):  #tostring()
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self._hakbun,  self._irum,
                                                       self._kor, self._eng, self._mat, self._edp,
                                                       self._total, self._avg, self._grade) 

    def convertDict(self):
        return {'hakbun':self._hakbun,  'irum' : self._irum, 'kor' : self._kor, 
                    'eng' : self._eng, 'mat':self._mat,  'edp':self._edp,  
                    'total' : self._total, 'avg' : self._avg, 'grade' : self._grade}