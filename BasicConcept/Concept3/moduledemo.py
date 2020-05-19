#moduledemo.py

# import math
# print(math.pi)

# from datetime import date
# print(date.today())

# import random
# print(random.randint(1, 10))

import requests

naver = requests.get('http://www.naver.com') #get방식 요청
print(naver.text)