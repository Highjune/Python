# import sqlite3
#   
# try :
#     conn = sqlite3.connect('../test.db') 
#     cursor = conn.cursor() #파이썬에서 데이터베이스 프로그래밍은 conn 후에는 다 cursor가 한다.
#       
#     cursor.execute('DROP TABLE IF EXISTS tblAddress')
#     sql = """
# CREATE TABLE tblAddress
# (
#     userid     TEXT    PRIMARY KEY,
#     name      TEXT    NOT NULL,
#     age         INTEGER,
#     address   TEXT
# )
# """    
#     cursor.execute(sql)
#       
#     cursor.close() #cursor만 close
# except Exception as ex:
#     print('Exception 발생=', ex.args[0])
#       
# finally :
#     conn.close()


import sqlite3
  
try :
    conn = sqlite3.connect('../test.db') 
    cursor = conn.cursor() #파이썬에서 데이터베이스 프로그래밍은 conn 후에는 다 cursor가 한다.

    cursor.execute("INSERT INTO tblAddress VALUES('june', '허강준', 14, '서울시 강남구 역삼동')")
    cursor.execute("INSERT INTO tblAddress VALUES('june2', '이강준', 24, '대구시 강남구 역삼동')")
    cursor.execute("INSERT INTO tblAddress VALUES('june3', '삼강준', 34, '부산시 강남구 역삼동')")
    cursor.execute("INSERT INTO tblAddress VALUES('june4', '사강준', 44, '울산시 강남구 역삼동')")
          
    conn.commit() #DML이므로 commit해야 한다.
    cursor.close()
      
except Exception as ex:
    print('Exception 발생=', ex.args[0])
      
finally :
    conn.close()
    
    
    