from pymongo import MongoClient

client = MongoClient('mongodb://admin:javamongodb@127.0.0.1')
db = client.test   #database

# etnews = db.etnews
# print(dir(etnews))
# etnews.delete_many({'author':'박태준'})

# print(db.etnews.find({'description':{'$regex':'코로나'}}).count())
db.etnews.delete_many({'description':{'$regex':'코로나'}})