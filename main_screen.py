
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog, ttk
import os

def admin_login():
    root.destroy()
    os.system("python admin_login.py")

def teacher_login():
    root.destroy()
    os.system("python teacher_login.py")
    
def invigilator_login():
    root.destroy()
    os.system("python invigilator_login.py")
    

def Main_Screen():
    global root
    root=tkinter.Tk()
    root.title("Main Menu")
    root.state('zoomed')
    #root.configure(bg='blue')
    root.geometry("1920x1080")
    photo=PhotoImage(file="ui/frt.png")
    photo2=PhotoImage(file="ui/admin_sign_in.png")
    photo3=PhotoImage(file="ui/teacher_sign_in.png")
    photo4=PhotoImage(file="ui/Invigilator_sign_in.png")
    photo5=PhotoImage(file="ui/exit1.png")
    btn= Button(
            root,
            image=photo,
            command="",
            border=0,
            text="",
            compound=TOP,
            )
    btn.pack()
    
    btn2= Button(
            root,
            image=photo2,
            command=admin_login,
            border=0,
            text="",
            compound=TOP,
            )
    btn2.pack()
    
    btn3= Button(
            root,
            image=photo3,
            command=teacher_login,
            border=0,
            text="",
            compound=TOP,
            )
    btn3.pack()
    
    btn4= Button(
            root,
            image=photo4,
            command=invigilator_login,
            border=0,
            text="",
            compound=TOP,
            )
    btn4.pack()
    
    btn5= Button(
            root,
            image=photo5,
            command=root.destroy,
            border=0,
            text="",
            compound=TOP,
            )
    btn5.pack()
    root.mainloop()
       
Main_Screen()
