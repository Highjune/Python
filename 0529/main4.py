import csv, cx_Oracle
from healthcenter import HealthCenter

with open('선별진료소목록.csv', 'rt', encoding='utf-8') as ptr:
    ptr.readline()   #첫줄 넘기기
    try:
        fieldnames = ['기준일시','가능여부','시도','시군구','의료기관명','주소','전화번호']
        mydict = csv.DictReader(ptr, fieldnames=fieldnames)
        num = 1
        mylist = []
        for row in mydict:
            obj_ = HealthCenter(num, row['기준일시'], row['가능여부'], row['시도'],
            row['시군구'], row['의료기관명'], row['주소'], row['전화번호'])
            mylist.append(obj_)
            num = num + 1
        
        # print(len(mylist))  #592
        conn = cx_Oracle.connect('scott/tiger@192.168.56.4:1521/XE')
        cursor = conn.cursor()
        for row in mylist:
            sql = "INSERT INTO HealthCenter(seq, mydate, enabled, sido, \
gugun, name, address, tel) \
VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}')"\
                    .format(int(row.seq), row.date, row.enable, row.sido, \
                        row.gugun, row.name, row.address, row.tel)
        # print(sql)
            cursor.execute(sql)
    except:
        print('Exception')
        conn.rollback()
    else :
        conn.commit()
        print('Insert Success')

    finally:
        conn.close()

# Create table HealthCenter
# (
# seq      NUMBER(4)   PRIMARY KEY,
# mydate   VARCHAR2(50) NOT NULL,
# enabled  CHAR(1)     NOT NULL,
# sido     VARCHAR2(20) NOT NULL,
# gugun     VARCHAR2(50),
# name      VARCHAR2(100) NOT NULL,
# address   VARCHAR2(200) NOT NULL,
# tel       VARCHAR2(60)  NOT NULL
# )