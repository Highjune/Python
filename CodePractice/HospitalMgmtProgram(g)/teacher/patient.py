class Patient(object):
    def __init__(self, bunho, code, days, age):
        self._bunho = bunho
        self._code = code
        self._days = days
        self._age = age
        
    @property
    def bunho(self): return self._bunho
    @property
    def code(self): return self._code
    @property
    def days(self): return self._days
    @property
    def age(self): return self._age
    
    @property
    def department(self): return self._department
    @department.setter
    def department(self, department): self._department = department
    
    @property
    def fee(self): return self._fee  #진찰비
    @fee.setter
    def fee(self, fee): self._fee = fee
    
    @property
    def goin(self): return self._goin  #입원비
    @goin.setter
    def goin(self, goin):  self._goin = goin
    
    @property
    def money(self): return self._money
    @money.setter
    def money(self, money): self._money = money
    
    def __str__(self):
        return '{0:3d}\t{1:7s}\t{2:<12,d}\t{3:6,d}\t{4:6,d}'.format(self._bunho,
                        self._department, self._fee, self._goin, self._money)