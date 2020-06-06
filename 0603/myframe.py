import tkinter
import tkinter.ttk
from functools import partial

class MyFrame(tkinter.Frame):
    def __init__(self, master, cursor):
        self._cursor = cursor

        self.treeview = tkinter.ttk.Treeview(master, selectmode='browse', 
            columns=["one", "two", "three", "four", "five"])
        self.treeview.pack(fill=tkinter.BOTH, side=tkinter.BOTTOM, expand=True) 

        self.treeview.column("#0", width=90, anchor="center")
        self.treeview.heading("#0", text='index')
        self.treeview.column("one", width=90, anchor="center")
        self.treeview.heading("one", text='ID')
        self.treeview.column("two", width=90, anchor="center")
        self.treeview.heading("two", text='Name')
        self.treeview.column("three", width=90, anchor="center")
        self.treeview.heading("three", text='CountryCode')
        self.treeview.column("four", width=90, anchor="center")
        self.treeview.heading("four", text='District')
        self.treeview.column("five", width=90, anchor="center")
        self.treeview.heading("five", text='Population')
        
        btn = tkinter.Button(master, text = 'Get Data', font=('Arial', 15), 
            command=partial(self.getData, self.treeview))
        btn.pack(side = tkinter.TOP)

    def getData(self, treeview):
        sql = "SELECT * FROM city WHERE countrycode = '%s'" % 'KOR'
        self._cursor.execute(sql)
        row = self._cursor.fetchone()
        cnt = 0
        while row : 
            treeview.insert('', 'end', values=row, text=str(cnt))
            cnt+=1
            row = self._cursor.fetchone()

