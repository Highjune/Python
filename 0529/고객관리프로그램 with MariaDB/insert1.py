def insert(conn, cursor) :
    try:
        userid = input('아이디 : ')
        name = input('이름 : ')
        gender = input('성별(남:1, 여:2) : ')
        city = input('거주지 : ')
        phone = input('전화번호 : ')
        sql = "INSERT INTO User VALUES('{}', '{}', '{}', '{}', '{}')"\
                    .format(userid, name, gender, city, phone)
        cursor.execute(sql)
    except : 
        print('Insert Exception')
        conn.rollback()
    else : 
        conn.commit()
        print('User Insert Success')