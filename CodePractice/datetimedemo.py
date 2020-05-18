# from datetime import date

#1st 방법
# print(date.today())

import time
# print(time.time())

# now = time.localtime(time.time())
# print(time.asctime(now))

#2nd 방법
#from datetime import datetime
#import time
#now = datetime.now()
#print(datetime.now())

#3rd 방법
# str = '지금은 %Y년 %m월 %d일 %A %p %I시 %M분 %S초 입니다.'
# print(time.strftime(str, time.localtime()))

import calendar

print(calendar.month(2020, 5))