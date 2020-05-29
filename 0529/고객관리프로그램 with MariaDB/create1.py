#create.py
def init(cursor):
    try:
        cursor.execute('DROP TABLE IF EXISTS User')
        sql = """
CREATE TABLE User
(
    userid       CHAR(8)             PRIMARY KEY,
    name        VARCHAR(20)     NOT NULL,
    gender      CHAR(1)             NOT NULL,
    city           VARCHAR(50)     NOT NULL,
    phone       CHAR(13)
)
"""
        cursor.execute(sql)
    except:
        print('Create Exception')
    else :
        print('Create Table Success')