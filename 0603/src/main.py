from tkinter import *
import tkinter.ttk 
import tkinter.font
import tkinter.messagebox

class MyFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title('회원 가입창')
        self.master.geometry('640x480+100+100')
        self.master.resizable(0, 1)
        self.pack(fill=BOTH, expand=True)
        
        fontExample = tkinter.font.Font(family="맑은 고딕", size=16, weight="bold", slant="italic")
        
        #아이디
        frame1 = Frame(self)
        frame1.pack(fill=X)
        
        lblId = Label(frame1, text='아이디', font=fontExample, width=10, bg='yellow')
        lblId.pack(side=LEFT, padx=10, pady=10)
        self.entryId = Entry(frame1, font=fontExample)
        self.entryId.pack(fill=X, padx=10, expand=True)
        
        #이름
        frame2 = Frame(self)
        frame2.pack(fill=X)
        
        lblName = Label(frame2, text='이름', font=fontExample, width=10, bg='aqua')
        lblName.pack(side=LEFT, padx=10, pady=10)
        self.entryName = Entry(frame2, font=fontExample)
        self.entryName.pack(fill=X, padx=10, expand=True)
        
        #성별
        frame3 = Frame(self)
        frame3.pack(fill=X)
        
        lblGender = Label(frame3, text='성별', font=fontExample, width=10, bg='magenta')
        lblGender.pack(side=LEFT, padx=10, pady=10)
        
        frame4= Frame(frame3)
        self.gender_variable = IntVar()
        radioFemale = Radiobutton(frame4, text='남성', font=fontExample, variable=self.gender_variable, 
                                  value=1)
        radioMale = Radiobutton(frame4, text='여성', font=fontExample, variable=self.gender_variable, 
                                value=2)
        btnRegister = Button(frame4, text='회원가입', font=fontExample, command=self.register)
        radioFemale.grid(row=0, column=1)
        radioMale.grid(row=0, column=2)
        btnRegister.grid(row=0, column=3)
        frame4.pack(fill=X, padx=10, expand=True)
        
        #나이 
        frame5 = Frame(self)
        frame5.pack(fill=X)
        lblAge = Label(frame5, text='나이', font=fontExample, width=10, bg='gray')
        lblAge.pack(side=LEFT, padx=10, pady=10)
        self.spinboxAge = tkinter.ttk.Spinbox(frame5, from_ = 20, to = 65, font=fontExample)
        self. spinboxAge.pack(fill=X, padx=10, expand=True)
        
        #거주지
        frame6 = Frame(self)
        frame6.pack(fill=X)
        lblCity = Label(frame6, text='거주지', font=fontExample, width=10, bg='lightblue')
        lblCity.pack(side=LEFT, padx=10, pady=10)
        self.comboCity = tkinter.ttk.Combobox(frame6, values=['서울','부산','광주','대구','인천','대전'], font=fontExample)
        self.comboCity.pack(fill=X, padx=10, expand=True)
        
        #자기소개
        frame7 = Frame(self)
        frame7.pack(fill=BOTH)
        lblDescription = Label(frame7, text='자기소개', font=fontExample, width=10, bg='orange')
        lblDescription.pack(side=LEFT, padx=10, pady=10)
        self.textDescription = Text(frame7, font=("맑은 고딕", 15))
        self.textDescription.pack(fill=BOTH, padx=10, pady=10, expand=True)
        
    def register(self):
        gender_ = None 
        if self.gender_variable.get() == 1: gender_ = '남성'
        elif self.gender_variable.get() == 2 : gender_ ='여성'
        record = {
            'userid' : self.entryId.get(),
            'username' : self.entryName.get(),
            'gender' : gender_,
            'userage' : self.spinboxAge.get(),
            'city' : self.comboCity.get(),
            'description' : self.textDescription.get("1.0","end")
        }
        print(record) 
        #mongod --dbpath ./data/db
        from pymongo import MongoClient
        try:
            conn = MongoClient('mongodb://admin:javamongodb@localhost')
            db = conn.test
            db.User.insert_one(record)
        except:
            print('Exception')
        else : 
            tkinter.messagebox.showinfo('insert', 'Insert Success')
        finally:
            conn.close()
            
        
app = Tk()

myframe = MyFrame(app)
app.mainloop()