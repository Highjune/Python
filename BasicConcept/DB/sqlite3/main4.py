# import sqlite3
# 
# try :
#     conn = sqlite3.connect("../test.db")
#     
#     cursor = conn.cursor()  #첫 레코드 바로 위에 커서가 위치
#     cursor.execute('SELECT * FROM tblAddress ORDER BY name DESC')
#     records = cursor.fetchall() #fetchall은 list인데, tuple의 list임
#     for record in records:
#         print('%s\t%s\t%d\t%s' % record) 
# #         print(record) #이걸로 보면 ( ) 즉, tuple인 것을 알 수 있다.
#     cursor.close()    
# except Exception as ex :
#     print('Exception = ', ex.args[0])
# finally :
#     conn.close()


import sqlite3

try :
    conn = sqlite3.connect("../test.db")
    
    cursor = conn.cursor()  #첫 레코드 바로 위에 커서가 위치
    cursor.execute('SELECT * FROM tblAddress ORDER BY name DESC')
    
    while True:
        record = cursor.fetchone()
        if record == None: break
        print('%s\t%s\t%d\t%s' % record)
            
    cursor.close()    
except Exception as ex :
    print('Exception = ', ex.args[0])
finally :
    conn.close()
    
    
    