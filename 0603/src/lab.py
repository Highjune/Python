import tkinter
import tkinter.ttk

app = tkinter.Tk()
app.title('TreeView Demo')
app.geometry('300x360')
app.resizable(0,0)
btn = tkinter.Button(app, text='Get Data', font=("맑은 고딕", 15))
btn.pack(side=tkinter.TOP)

#TreeView 를 GUI에 붙이기
treeview = tkinter.ttk.Treeview(app, selectmode='browse')
treeview.pack(fill=tkinter.BOTH)

treeview["columns"] = ("one", "two", "three")
# treeview["show"] = 'heading'

treeview.column("#0", width=90, anchor="w")
treeview.column("one", width=90, anchor="center")
treeview.column("two", width=90, anchor="center")
treeview.column("three", width=90, anchor="center")

treeview.heading("#0", text="index")
treeview.heading("one", text="ID")
treeview.heading("two", text="Name")
treeview.heading("three", text="Age")

treeview.insert('', 'end', values=("jimin", "한지민", 24), text='r1')
treeview.insert('', 'end', values=("javasoft", "박지민", 25), text='r2')
treeview.insert('', 'end', values=("javaexpert", "홍지민", 28), text='r3')
treeview.insert('', 'end', values=("pythonexpert", "김지민", 30), text='r4')
treeview.insert('', 'end', values=("springexpert", "송지민", 34), text='r5')
app.mainloop()