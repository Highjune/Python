import pymysql, tkinter, myframe

def main(cursor):
    app = tkinter.Tk()
    app.title("Korean Cities Information")
    app.geometry('640x480')
    app.resizable(1,1)
    myframe.MyFrame(app, cursor)
    app.mainloop()

if __name__ == "__main__":
    # try:
    conn = pymysql.connect(host='localhost', user='root', password='javamariadb', 
                                        database='world')
    cursor = conn.cursor()
    main(cursor)
    # except Exception as ex:
        # print('Exception = ', ex.args[0])

    # finally : 
    #     conn.close()