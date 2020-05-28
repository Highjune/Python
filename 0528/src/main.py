#main.py

import json
from pymongo import MongoClient

#Database Connection
# client = MongoClient('localhost', 27017, {'user':'admin', 'password':'javamongodb'}, maxPoolSize=50)
client = MongoClient('mongodb://admin:javamongodb@localhost')
# print(client)
db = client.test   #database 연결
students = db['dept']   #collection 연결

# print(students)
# print(type(students))
    
cursor = students.find({'deptno':20}, {'_id':False, 'dname':True})
# print(type(cursor))
deptname = None
for i, document in enumerate(cursor) : 
    deptname = document['dname']
    
print('20번 부서의 이름은 ', deptname, '입니다.')