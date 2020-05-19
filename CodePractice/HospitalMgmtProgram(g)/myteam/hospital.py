class Hospital:
    
    def __init__(self, num,code,ibwonilsu,age):
        self._num= num
        self._code= code
        self._ibwonilsu= ibwonilsu
        self._age= age
        
    @property
    def num(self): return self._num
    @property
    def code(self): return self._code
    @property
    def ibwonilsu(self): return self._ibwonilsu
    @property
    def age(self): return self._age
   
    @property
    def jindept(self): return self._jindept #getter
    @jindept.setter
    def jindept(self,jindept): self._jindept=jindept # setter
    
    @property
    def jinchalfee(self): return self._jinchalfee #getter
    @jinchalfee.setter
    def jinchalfee(self,jinchalfee): self._jinchalfee=jinchalfee # setter
    
    @property
    def ibwonfee(self): return self._ibwonfee #getter
    @ibwonfee.setter
    def ibwonfee(self, ibwonfee): self._ibwonfee=ibwonfee # setter
    
    @property
    def jinryofee(self): return self._jinryofee #getter
    @jinryofee.setter
    def jinryofee(self,jinryofee): self._jinryofee=jinryofee # setter
    
    def __str__(self): #toString()
        return '{}\t{}\t{}\t{}\t{}'.format(self._num,self._jindept,self._jinchalfee,self._ibwonfee,self._jinryofee)