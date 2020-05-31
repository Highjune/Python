class Point : 
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y

    def toString(self):
        return '(x, y) = ({}, {})'.format(self._x, self._y)

    def __str__(self):
        return '(x, y) = ({}, {})'.format(self._x, self._y)

    def add(self, another):
        self._x = self._x + another._x
        self._y = self._y + another._y
        print('called add')

    def __add__(self, another):
        self._x = self._x + another._x
        self._y = self._y + another._y
        print('called add')

p1 = Point(100, 150)
p2 = Point(500, 500)
#p1.add(p2)
p1 + p2
print(p1)
# print(p1)
# print(p1.toString())