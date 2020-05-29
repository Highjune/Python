import pymysql

try:
    conn = pymysql.Connection(host='localhost', user = 'root', passwd = 'javamariadb',
                db = 'world', port = 3306)
    cursor = conn.cursor()
    cursor.execute('SELECT version(), now()')
    # print(cursor)
    result = cursor.fetchone()
    print('version = %s, now = %s' % (result))
except:
    print('Exception')
else:
    pass
finally:
    cursor.close()
    conn.close()