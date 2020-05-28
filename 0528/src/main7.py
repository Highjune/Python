from pymongo import MongoClient

client = MongoClient('mongodb://admin:javamongodb@127.0.0.1')
db = client.test   #database

db.students.update_many({'irum':'한송이'}, {'$set':{'kor':100}})

print(db.students.find_one({'irum':'한송이'}))