import time

def getToday():
    sm = time.localtime()
    return sm.tm_year, sm.tm_mon, sm.tm_mday

year, month, day = getToday()
print('오늘은 {}년 {}월 {}일입니다.'.format(year, month, day))