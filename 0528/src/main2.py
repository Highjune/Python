from pymongo import MongoClient

#1. Database Connection
username = 'admin'
password = 'javamongodb'
host = '127.0.0.1'
client = MongoClient('mongodb://%s:%s@%s' % (username, password, host))
# print(type(client))
# print(dir(client))
# print(client.list_database_names())   #show dbs

#2. database Connection
# db = client.test
db = client['test']
# print(type(db))   #database
# print(dir(db))
# print(db.list_collection_names())
# movie_ = {
#     '제목' : '너의 이름은',
#     '감독' : '신카이 마코토',
#     '배우' : ['카미키 류노스케', '카미시라이시 모네'],
#     '년도' : 2017,
#     '러닝타임': 106
# }

movies = [
    {'제목':'글래디에이터', '감독':'리틀리 스콧', '배우': ['러셀 크로우', '호아킨 피닉스', '코니 닐슨', '올리버 리드'], 
        '년도':2000, '러닝타임':154},
    {'제목':'언더워터', '감독':'윌리엄 유뱅크', '배우':['크리스틴 스튜어트', '뱅상 카셀', 'T.J. 밀러'], 
        '년도':2020, '러닝타임':95},
    {'제목':'살인의 추억', '감독':'봉준호', '배우' : ['송강호', '김상경'], 
        '년도':2003, '러닝타임':132}
]
# id_ = db.movie.insert_one(movie_)
db.movie.insert_many(movies)






