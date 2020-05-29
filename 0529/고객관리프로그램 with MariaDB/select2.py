def read(cursor):
    try:
        userid = input('찾는 회원아이디 : ')
        sql = "SELECT userid, name, gender, city, phone FROM User \
                WHERE userid = '{}'".format(userid)
        cursor.execute(sql)
        row = cursor.fetchone()
        if row == None : print('User Not Found')
        else : print(row)
    except :
        print('Select Exception ')