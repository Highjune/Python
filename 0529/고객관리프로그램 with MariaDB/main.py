import sys, pymysql, create1, insert1, select1, select2, update1, delete1

def showmenu():
    print("1 : 초기화")
    print("2 : 회원가입")
    print("3 : 전체 회원명단 보기")
    print("4 : 회원검색하기")
    print("5 : 회원정보변경하기")
    print("6 : 회원탈퇴하기")
    print("9 : 종료하기")
    return int(input(">>선택 : "))

def process(choice):
    if choice == 1:  create1.init(cursor)
    elif choice == 2 : insert1.insert(conn, cursor)
    elif choice == 3 : select1.readAll(cursor)
    elif choice == 4 : select2.read(cursor)
    elif choice == 5 : update1.update(conn, cursor)
    elif choice == 6 : delete1.delete(conn, cursor)

if __name__ == '__main__':
    try:
        conn = pymysql.Connection(host = 'localhost', 
            user = 'jimin', passwd = 'jimin', db = 'mydb', port = 3306)
        cursor = conn.cursor()
        while True: 
            choice = showmenu()
            if choice == 9 : 
                print('Bye')
                sys.exit(0)
            process(choice)
    except:
        print('Main Exception')
    finally : 
        conn.close()