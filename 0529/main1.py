import pymysql

try:
    conn = pymysql.Connection(host = '192.168.56.2', user = 'root', passwd = 'javamariadb',
               db = 'world')
    cursor = conn.cursor()
    sql = """
            SELECT id, name, countrycode, district, population
            FROM city
            WHERE countrycode = 'KOR'
"""
    cursor.execute(sql)
    row = cursor.fetchone()
    while True:
        if row == None : break
        print(row[0], row[1], row[2], row[3], row[4])
        row = cursor.fetchone()

except:
    print('Exception')
else :
    pass
finally:
    conn.close()