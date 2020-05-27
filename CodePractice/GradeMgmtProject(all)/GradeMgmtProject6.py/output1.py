import sqlite3
from student import Student

def myoutput1(mylist):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS Student')
        sql = """
CREATE TABLE Student(
    hakbun        TEXT       PRIMARY KEY,
    irum            TEXT       NOT NULL,
    kor              INT       NOT NULL,
    eng               INT       NOT NULL,
    mat              INT       NOT NULL,
    edp              INT       NOT NULL,
    total              INT       NOT NULL,
    avg               REAL       NOT NULL,
    grade           TEXT       NOT NULL
)
"""
        cursor.execute(sql)
        for s in mylist:
            sql = "INSERT INTO Student VALUES('{}', '{}', {}, {}, {}, {}, {}, {}, '{}')"\
                .format(s.hakbun, s.irum, s.kor, s.eng, s.mat, s.edp, s.total, s.avg, s.grade)
            # print(sql)
            cursor.execute(sql)
    except:
        print('SQL Exception')
    else :
        conn.commit()
        print("insert success")
    finally:
        conn.close()