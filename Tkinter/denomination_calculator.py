from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk

root = Tk()
root.geometry("650x400")
root.title("Denomination calculator")
root.configure(bg="light blue")

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(
    root,
    text="hey user! welcome to denomination counter application,",
    bg="light blue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count? "
    )
    if MsgBox == "ok":
        topwin()

button1 = Button(
    root,
    text="let's get started!",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    label = Label(top, text="enter total amount", bg="light grey")
    entry = Entry(top)
    lbl = Label(
        top,
        text="here are number notes for each denomination",
        bg = "light grey"
    )
    

