import requests, json
from pymongo import MongoClient

try:
    url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'
    response = requests.get(url)
    json_data = json.loads(response.text)
    stores = json_data['stores']   #dict list
    list_ = []
    for store in stores:
        type__ = None
        type_ = store['type']
        if type_ == '01' : type__ = '약국'
        elif type_ == '02' : type__ = '우체국'
        elif type_ == '03' : type__ = '농협'
     
        remain_stat_ = None
        stock_at_ = None
        if store['code'] == '12848344': 
            remain_stat_ = None
            stock_at_ = None 
        else : 
            remain_stat_ = store['remain_stat']
            stock_at_ = store['stock_at']
     
        data_ = {
           '약국이름' : store['name'],
           '약국주소' : store['addr'],
            '재고상태' : remain_stat_,  
           '입고시간' : stock_at_, 
            '판매처유형' : type__
        }
        list_.append(data_)
    
    client = MongoClient('mongodb://admin:javamongodb@127.0.0.1')
    db = client.test
    db.MaskInfo.insert_many(list_)
except:
    print('Exception')
else : 
    print('Insert Success')
finally : 
    client.close()