
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 20:36:35 2021

@author: DESKTOP-4E3MIV5
"""

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
def btnclick():
    messagebox.showinfo("Message","button is clicked")

def main_screen():
    root.destroy()
    os.system("python main_screen.py")
    
def Main_Menu():
    global root
    root=tkinter.Tk()
    root.title("Teacher")
    root.geometry("1920x1080")
    photo=PhotoImage(file="ui/teacher_panel.png")
    photo2=PhotoImage(file="ui/registration.png")
    photo3=PhotoImage(file="ui/mark_attendance.png")
    photo4=PhotoImage(file="ui/invigilation.png")
    back=PhotoImage(file="ui/back.png")
    photo5=PhotoImage(file="ui/exit.png")
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
            image=photo3,
            command=mark_attendance,
            border=0,
            text="",
            compound=TOP,
            )
    btn3.pack()
    
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




