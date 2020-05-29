def readAll(cursor):
    try:
        cursor.execute("SELECT userid, name, gender, city, phone FROM User ORDER BY name DESC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except:
        print('Select Exception')