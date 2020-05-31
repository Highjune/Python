# import mydate
# 
# if __name__ == '__main__':
#     print(mydate.mytoday())

# from mydate import mytoday
# if __name__ == '__main__':
#     print(mytoday())

# from mydate import *
# if __name__ == '__main__':
#     print(mytoday())

# from com import *
# 
# if __name__ == '__main__':
#     print(myadd.add(5, 9))
#     print(mymulti.multiply(5, 9))

from com import myadd as a
from com import mymulti as b
if __name__ == '__main__':
    print(a.add(5, 9))
    print(b.multiply(5, 9))
