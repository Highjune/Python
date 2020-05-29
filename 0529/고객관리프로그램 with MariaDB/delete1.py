def delete(conn, cursor):
    try:
        userid = input('삭제할 회원아이디 : ')
        sql = "DELETE FROM User WHERE userid = '{}'".format(userid)
        cursor.execute(sql)
    except:
        print('Delete Exception')
        conn.rollback()
    else :
        conn.commit()
        print("Delete Success")