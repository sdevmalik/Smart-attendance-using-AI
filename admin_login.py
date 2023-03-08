
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image,ImageTk
import os
import mysql.connector as mysql




def main_screen():
    root.destroy()
    os.system("python main_screen.py")
    
def main():
    global root
    
    root = Tk()
    root.title("Admin Login")
    root.geometry("1920x1080")
    root.state('zoomed')
    
    
    global uid
    global pid
    
    photo=PhotoImage(file="ui/admin_login.png")
    photo2=PhotoImage(file="ui/login1.png")
    photo3=PhotoImage(file="ui/back1.png")
    
    btn= Button(
                root,
                image=photo,
                command="",
                border=0,
                text="",
                compound=TOP,
                )
    btn.pack()
    
    username = Label(root, text='Username',font=('bold',16))
    username.place(x=450,y=430); 
    
    password = Label(root, text='Password',font=('bold',16))
    password.place(x=450,y=480); 
    
    uid=Entry(root,width="50");
    uid.place(x=600,y=430)
    
    pid=Entry(root,width="50",show='*');
    pid.place(x=600,y=480)
    
    btn2= Button(
                root,
                image=photo2,
                command=insert,
                border=0,
                text="",
                compound=TOP
                )
    btn2.place(x=430,y=550)
    btn3= Button(
                root,
                image=photo3,
                command=main_screen,
                border=0,
                text="",
                compound=TOP
                )
    btn3.place(x=730,y=550)
    root.mainloop()
    
def insert():
    user=uid.get()
    pas=pid.get()
    if (user=="" or pas==""):
        messagebox.showinfo("Error","Enter Username and Password")
    else:
        con=mysql.connect(host="localhost",user="root",password="SaS@root1",database="sas")
        cursor=con.cursor()
        flag=0
        
        cursor.execute("SELECT * FROM admin where admin_username='" + user + "'")
        
        for row in cursor.fetchall():
            if row[1]==pas:
                flag=1
                break
    if flag==1:
        messagebox.showinfo("Login","Login Successfull")
        root.destroy()
        os.system("python admin_panel.py")
    else:
        messagebox.showinfo("Login Failed","Incorrect Username or Password")
        uid.delete(0,END)
        pid.delete(0,END)
    
main()
  
