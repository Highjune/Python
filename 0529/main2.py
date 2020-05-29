import mysql.connector as mc
from mysql.connector import Error

try:
    conn = mc.connect(user='root', password='javamysql', host = '192.168.56.4', database='world')
    if conn.is_connected():
        print(conn.get_server_info())   #5.6.47
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, countrycode, district, population \
                                FROM city WHERE countrycode = 'KOR'")
        for id, name, countrycode, district, population in cursor:
            print('{}\t{}\t{}\t{}\t{}'.format(id, name, countrycode, district, population))
except Error as e:
    print('Exception = ', e)
finally:
    pass
