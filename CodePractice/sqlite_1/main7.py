import requests
import xml.etree.ElementTree as ET
import sqlite3

try: 
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Article')
    sql = """
CREATE TABLE Article
(
    guid               INTEGER    PRIMARY KEY,
    title                TEXT          NOT NULL,
    description    TEXT           NOT NULL,
    author            TEXT          NOT NULL,
    pubDate         TEXT          NOT NULL
)
"""
    cursor.execute(sql)
except : 
    print('Sql Exception')
else : 
    try:
        response = requests.get('http://rss.etnews.com/Section901.xml')
        xml_ = ET.fromstring(response.text)   #Element
        items = xml_.iter('item')
        for item in items :
            guid = int(item.find('guid').text.strip())
            title = item.find('title').text.strip()
            title = title.replace("'", "''")
            descript = item.find('description').text.strip()
            descript = descript.replace("'", "''")
            author = item.find('author').text.strip()
            pubDate = item.find('pubDate').text.strip()
            sql = "INSERT INTO Article VALUES({}, '{}', '{}','{}', '{}')".format(guid, title, descript, author, pubDate) 
#             print(sql)
            cursor.execute(sql)
    except:
        print('SQL Exception')
    else : 
        conn.commit()
        print('insert success')
finally : 
    conn.close()