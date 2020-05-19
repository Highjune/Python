#main3랑
class Point:
    def __init__(self, x=0, y=0): #기본인자
        self._x = x
        self._y = y

    def __str__(self):  #toString
        return '(x, y) = ({}, {})'.format(self._x, self._y)

    def __len__(self):
        mylist = []
        mylist.append(self._x)
        mylist.append(self._y)
        return len(mylist)

    def __add__(self, other):
        # return Point(self._x + other._x, self._y + other._y)
        return Point(self._x + other, self._y + other)

    def __radd__(self, other):
        return Point(self._x + other, self._y + other)

    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y)

    def __mul__(self, other):
        return Point(self._x * other._x, self._y * other._y)

    def __mod__(self, other):
        return Point(self._x % other._x, self._y % other._y)

    def __truediv__(self, other):
        return Point(self._x / other._x, self._y / other._y)

