import tkinter
import tkinter.font
import tkinter.messagebox

def confirm():
    if radioValue.get() == 1:
        tkinter.messagebox.showinfo('gender', '남성이군요')
    elif radioValue.get() == 2:
        tkinter.messagebox.showinfo('gender', '여성이군')

app = tkinter.Tk()
app.title('RadioButton Demo')
app.geometry('300x300')
app.resizable(0, 0)

fontExample = tkinter.font.Font(family="Arial", size=16, weight="bold", slant="italic")

radioValue = tkinter.IntVar()
radioMale = tkinter.Radiobutton(app, text = '남성', value=1, variable=radioValue, font=fontExample)
radioFemale = tkinter.Radiobutton(app, text = '여성', value=2, variable=radioValue, font=fontExample) 
radioMale.grid(row=0, column=0)
radioFemale.grid(row=0, column=1)

btn = tkinter.Button(app, text='OK', command=confirm, font=fontExample)
btn.grid(row=1, column=1)
app.mainloop()



