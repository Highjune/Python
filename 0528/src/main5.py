from pymongo import MongoClient

# try:
client = MongoClient('mongodb://admin:javamongodb@127.0.0.1')
db = client.test   #database
maskinfo = db.MaskInfo  #collection
#     print(students.find({'irum':'한송이'},{'_id':False}).count())
# for document in students.find({'kor': {'$gt':80}}, {'_id':False}) :
#     print(document) 
for document in maskinfo.find({'약국주소' : {'$regex':'역삼동'}}, {'_id':0, '약국이름':1, '약국주소':1}):
    print(document)
# except  :
#     print('Exception')
# finally : 
#     client.close()