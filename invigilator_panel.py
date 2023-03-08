
import tkinter
import MySQLdb
from tkinter import *
from tkinter import messagebox, filedialog, ttk
import os
import cv2
import dlib
import numpy as np
from imutils import face_utils
from decimal import Decimal
import math
import sys
import time
from playsound import playsound
import winsound



def registration():
    os.system("python registration.py")
    
def mark_attendance():
    os.system("python attendance.py")    

def invigilation():
    os.system("python headpose.py")
    
def invigilation2():
    os.system("python eye_gaze.py")
    
def btnclick():
    messagebox.showinfo("Message","button is clicked")

def main_screen():
    root.destroy()
    os.system("python main_screen.py")
    
def Main_Menu():
    global root
    root=tkinter.Tk()
    root.title("Invigilator")
    root.geometry("1920x1080")
    photo=PhotoImage(file="ui/invigilator_panel.png")
    photo2=PhotoImage(file="ui/registration.png")
    photo3=PhotoImage(file="ui/mark_attendance.png")
    photo4=PhotoImage(file="ui/invigilation1.png")
    back=PhotoImage(file="ui/back.png")
    photo5=PhotoImage(file="ui/exit.png")
    photo10=PhotoImage(file="ui/invigilation2.png")
    btn= Button(
            root,
            image=photo,
            command=btnclick,
            border=0,
            text="",
            compound=TOP,
            )
    btn.pack()
    
    btn3= Button(
            root,
            image=photo4,
            command=invigilation,
            border=0,
            text="",
            compound=TOP,
            )
    btn3.pack()
    
    btn10= Button(
            root,
            image=photo10,
            command=invigilation2,
            border=0,
            text="",
            compound=TOP,
            )
    btn10.pack()
    
    btn4= Button(
            root,
            image=back,
            command=main_screen,
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
        
Main_Menu()




