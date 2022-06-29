# import required modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
# contrast border thumbnail 
root = Tk()
root.title("Simple Photo Editor")
root.geometry("950x500")
root['bg']='#1B2430'
# create functions
def selected():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
    img = Image.open(img_path)
    img.thumbnail((640, 350))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image=img1                                                                                                                                                                                                                
def blur(event):
    global img_path, img1, imgg
    for m in range(0, v1.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = img.filter(ImageFilter.BoxBlur(m))
            img1 = ImageTk.PhotoImage(imgg) 
            canvas2.create_image(300, 210, image=img1)
            canvas2.image=img1
def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Brightness(img)
            img2 = imgg.enhance(m)
            img3 = ImageTk.PhotoImage(img2)
            canvas2.create_image(300, 210, image=img3)
            canvas2.image=img3
def contrast(event):
    global img_path, img4, img5
    for m in range(0, v3.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Contrast(img)
            img4 = imgg.enhance(m)
            img5 = ImageTk.PhotoImage(img4)
            canvas2.create_image(300, 210, image=img5)
            canvas2.image=img5
def rotate_image(event):
        global img_path, img6, img7
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img6 = img.rotate(int(rotate_combo.get()))
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(300, 210, image=img7)
        canvas2.image=img7
        
def flip_image(event):
        global img_path, img8, img9
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        if flip_combo.get() == "LEFT-RIGHT":
            img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_combo.get() == "TOP-BOTTOM":
            img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
        img9 = ImageTk.PhotoImage(img8)
        canvas2.create_image(300, 210, image=img9)
        canvas2.image=img9   
def image_border(event):
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = ImageOps.expand(img, border=int(border_combo.get()), fill=95)
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 210, image=img11)
    canvas2.image=img11    
img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None
def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    #file=None
    ext = img_path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    if file: 
            if canvas2.image==img1:
                imgg.save(file)
            elif canvas2.image==img3:
                img2.save(file)
            elif canvas2.image==img5:
                img4.save(file)
            elif canvas2.image==img7:
                img6.save(file)
            elif canvas2.image==img9:
                img8.save(file)
            elif canvas2.image==img11:
                img10.save(file)        
# create labels, scales and comboboxes
blurr = Label(root, text="Blur:",fg='white', bg='#1B2430',font=("calibri 17"),anchor='e')
blurr.place(x=5, y=4)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur) 
scale1.place(x=60, y=8)
bright = Label(root, text="Brightness:",fg='white',bg='#1B2430', font=("calibri 17"))
bright.place(x=175, y=4)
v2 = IntVar()   
scale2 = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness) 
scale2.place(x=290, y=8)
contrast = Label(root, text="Contrast:",fg='white',bg='#1B2430', font=("calibri 17"))
contrast.place(x=410, y=4)
v3 = IntVar()   
scale3 = ttk.Scale(root, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=contrast) 
scale3.place(x=520, y=8)
rotate = Label(root, text="Rotate:",fg='white',bg='#1B2430', font=("calibri 17"))
rotate.place(x=690, y=8)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=('calibri 10'))
rotate_combo.place(x=770, y=15)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)
flip = Label(root, text="Flip:",fg='white',bg='#1B2430', font=("calibri 17"))
flip.place(x=720, y=50)
values1 = ["LEFT-RIGHT", "TOP-BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=('calibri 10'))
flip_combo.place(x=770, y=57)
flip_combo.bind("<<ComboboxSelected>>", flip_image)
border = Label(root, text="Add border:",fg='white',bg='#1B2430', font=("calibri 17"))
border.place(x=650, y=92)
values2 = [i for i in range(10, 45, 2)]
border_combo = ttk.Combobox(root, values=values2, font=("calibri 10"))
border_combo.place(x=770, y=99)
border_combo.bind("<<ComboboxSelected>>", image_border)
# create canvas to display image
canvas2 = Canvas(root, bg='#1B2430',width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=60)
# create buttons
btn1 = Button(root, text="Select Image",width=12, bg='black', fg='white', font=('calibri 15'), relief=GROOVE, command=selected)
btn1.place(x=650, y=300)
btn2 = Button(root, text="Save", width=12, bg='black', fg='white', font=('calibri 15'), relief=GROOVE, command=save)
btn2.place(x=790, y=300)
btn3 = Button(root, text="Exit", width=12, bg='black', fg='white', font=('calibri 15'), relief=GROOVE, command=root.destroy)
btn3.place(x=720, y=350)
root.mainloop()