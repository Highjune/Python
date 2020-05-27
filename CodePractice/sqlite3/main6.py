#books.xml --> test.db > books table
import xml.etree.ElementTree as ET
import sqlite3

try:
    conn = sqlite3.connect('../test.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS books')
    sql = """
CREATE TABLE books
(
    id                        TEXT            PRIMARY KEY,
    author                 TEXT            NOT NULL,
    title                     TEXT            NOT NULL,
    genre                   TEXT            NOT NULL,
    price                     REAL            NOT NULL,
    publish_date        TEXT            NOT NULL,
    description           TEXT            NOT NULL
)
"""
    cursor.execute(sql)
except:
    print('SQL Exception')
else :
    try:
        xml_ = ET.parse("../books.xml")   #Element Tree
        root = xml_.getroot()                     #Element
        books = root.findall('book')           #List of tuple
        for book in books:
            id = book.attrib['id'].strip()
            author = book.find('author').text.strip()
            author = author.replace("'", "''")
            title = book.find('title').text.strip()
            title = title.replace("'", "''")
            genre = book.find('genre').text.strip()
            price = float(book.find('price').text.strip())
            publish_date = book.find('publish_date').text.strip()
            description = book.find('description').text.strip()
            description = description.replace("'", "''")
            sql = "INSERT INTO books VALUES('{}', '{}', '{}', '{}', {}, '{}', '{}')".format(id, author, title, genre, price, publish_date, description)
#             print(sql)
            cursor.execute(sql)
    except :
        print('XML Exception')
    else : 
        conn.commit()
        print('save successfully')
finally:
    conn.close()
    
    
    
    
    