# -*- coding: utf-8 -*-

import tkinter
from tkinter import *
from tkinter import messagebox
import os

def invigilation():
    os.system("python headpose.py")
    
def invigilator():
    
    def main_menu():
        root.destroy()
        os.system("python main_menu.py")
    
    root=tkinter.Tk()
    #root.configure(bg='blue')
    root.geometry("1920x1080")
    photo=PhotoImage(file="ui/invigilator_panel.png")
    photo2=PhotoImage(file="ui/invigilation1.png")
    photo3=PhotoImage(file="ui/invigilation2.png")
    photo4=PhotoImage(file="ui/signout.png")
    btn= Button(
            root,
            image=photo,
            border=0,
            text="",
            compound=TOP,
            )
    btn.pack()
    
    btn2= Button(
            root,
            image=photo2,
            command=invigilation,
            border=0,
            text="",
            compound=TOP,
            )
    btn2.pack()
    
    btn3= Button(
            root,
            image=photo3,
            command=invigilation,
            border=0,
            text="",
            compound=TOP,
            )
    btn3.pack()
    
    btn4= Button(
            root,
            image=photo4,
            command=main_menu,
            border=0,
            text="",
            compound=TOP,
            )
    btn4.pack()
    root.mainloop()
    
    
       
invigilator()
