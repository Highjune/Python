#CheckButton
import tkinter
import tkinter.font
import tkinter.messagebox

def buy():
    str_ = 'Ordered Fruits : '
    for i in check_value : 
        if check_value[i].get() == True:
            str_ += fruits[i] + ','
#             print(fruits[i])
    tkinter.messagebox.showinfo('주문내용', str_.rstrip(','))
        
app = tkinter.Tk()
app.title('CheckButton Demo')
app.geometry('300x300')
app.resizable(0, 0)
fruits = {0:'Apple', 1:'Mango', 2:'Grape', 3:'PineApple', 4:'Melon'}
check_value = {}
fontExample = tkinter.font.Font(family="Arial", size=16, weight="bold", slant="italic")
for i in range(len(fruits)):
    check_value[i] = tkinter.BooleanVar()
    tkinter.Checkbutton(app, variable=check_value[i], text=fruits[i], 
                        font=fontExample).pack(anchor=tkinter.W)
    
btn = tkinter.Button(app, text='Order', command=buy, font=fontExample).pack(anchor=tkinter.S)
app.mainloop()


