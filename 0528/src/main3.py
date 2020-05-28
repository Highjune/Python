import xml.etree.ElementTree as ET
from pymongo import MongoClient
import requests

try:
    client = MongoClient('mongodb://admin:javamongodb@127.0.0.1')
    db = client.test   #test database
    response = requests.get('http://rss.etnews.com/Section901.xml')
    xml_ = ET.fromstring(response.text)
#     print(xml_.tag)    #Element, rss
#     print(dir(xml_))
    channel_ = xml_.find('channel')
#     print(channel_.tag)   #channel, Element
    for item in channel_.findall('item') : 
        title = item.find('title').text
        description = item.find('description').text 
        author = item.find('author').text 
        pubDate = item.find('pubDate').text
        db.etnews.insert_one({
            'title ' : title,  'description' : description, 'author' : author, 'pubDate' : pubDate
        })
except:
    print('Exception 발생')
else :
    print('Insert Success')
