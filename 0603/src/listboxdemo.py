import tkinter
import tkinter.font
import tkinter.messagebox

app = tkinter.Tk()
app.title('Listbox Demo')
app.geometry('300x300')
app.resizable(0, 0)

fontExample = tkinter.font.Font(family="맑은 고딕", size=16, weight="bold", slant="italic")
listbox = tkinter.Listbox(app, selectmode='extended', height=0, font=fontExample)
listbox.insert(0, 'Apple')
listbox.insert(1, 'Mango')
listbox.insert(2, 'Grape')
listbox.insert(3, 'FineApple')
listbox.insert(4, 'Melon')
listbox.pack()
app.mainloop()