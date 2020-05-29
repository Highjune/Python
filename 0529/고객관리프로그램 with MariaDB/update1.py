def update(conn, cursor) : 
    try:
        userid = input('회원아이디 : ')
        city = input('변경할 거주지 : ')
        phone = input('변경할 전화번호 : ')
        sql = "UPDATE User SET city = '{}', phone = '{}' WHERE userid = '{}'"\
            .format(city, phone, userid)
        cursor.execute(sql)
    except:
        print('Update Exception')
        conn.rollback()
    else : 
        conn.commit()
        print('Update Success')
