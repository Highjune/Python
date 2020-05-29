class HealthCenter:
    def __init__(self, seq, date, enable, sido, gugun, name, address, tel):
        self._seq = seq
        self._date = date
        self._enable = enable
        self._sido = sido
        self._gugun = gugun
        self._name = name
        self._address = address
        self._tel = tel
    
    @property
    def seq(self): return self._seq
    @property
    def date(self): return self._date
    @property
    def enable(self): return self._enable
    @property
    def sido(self): return self._sido
    @property
    def gugun(self): return self._gugun
    @property
    def name(self): return self._name
    @property
    def address(self): return self._address
    @property
    def tel(self): return self._tel

    def __str__(self):
        return [self._seq, self._date, self._enable, self._sido, self._gugun, 
        self._name, self._address, self._tel]
    