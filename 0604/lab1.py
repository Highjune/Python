import tkinter
from PIL import ImageTk
import qrcode
import tkinter.filedialog

def generate():
    imgLabel.qr_code_img = qrcode.make(entry.get())
    img_width, img_height = imgLabel.qr_code_img.size
    imgLabel.tk_img = ImageTk.PhotoImage(imgLabel.qr_code_img)
    imgLabel.config(image =  imgLabel.tk_img, width=img_width, height=img_height)
    imgLabel.pack()

def save():
    filename = tkinter.filedialog.asksaveasfilename(title='다른 이름으로 저장', 
                                                                         initialfile='qrcode.png')
    if filename :
        imgLabel.qr_code_img.save(filename)
        print('Save Success')

    else : print('Save Failure')

def exit():
    # app.quit()   #앱을 숨김
    app.destroy()

app = tkinter.Tk()
app.title('QRCode Demo')
input_area = tkinter.Frame(app, relief=tkinter.RAISED, bd=2)
image_area = tkinter.Frame(app, relief=tkinter.SUNKEN, bd=2)

encode_text = tkinter.StringVar()
entry = tkinter.Entry(input_area, textvariable=encode_text, 
                    font=("Arial", 20))
entry.pack(side=tkinter.LEFT)
btn = tkinter.Button(input_area, text='Convert', command=generate,
            font=("Arial", 20)).pack(side=tkinter.LEFT)
input_area.pack(pady=5)

imgLabel = tkinter.Label(image_area)
image_area.pack(padx=3, pady=3)

menubar = tkinter.Menu(app)
filemenu = tkinter.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Save', command=save)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=exit)
app.config(menu=menubar)
app.mainloop()

