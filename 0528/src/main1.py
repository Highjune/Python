import json
from pymongo import MongoClient

client = MongoClient('mongodb://admin:javamongodb@127.0.0.1')
db = client.test;
students = db['students']
cursor = students.find({
        'irum' : '한송이'
    }, {'_id':False})
for i, document in enumerate(cursor):
    print(i, document)