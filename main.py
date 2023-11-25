import mysql.connector
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='dbnbg3jt@',
    port='3306',
    database='master'

)

mycursor=conn.cursor()


def on_enterU(e):
    Username1.delete(0,'end')

def on_leaveU(e):
    if Username1.get()=='':
        Username1.insert(0,'Enter Username')

def on_enterP(e):
    Password1.delete(0, 'end')
    Password1.config(show='*')

def on_leaveP(e):
    if Password1.get() == '':
       # Password1.config(show=" ")
        Password1.insert(0, 'Enter Password')
def login():
    username=Username1.get()
    password = Password1.get()

    if username== 'admin' and password=='dbnbg3jt':
        root.destroy()
        import mainpage
    else:
         tkinter.messagebox.showerror('Window Title', 'incorrect username or password')

root=Tk()
root.title("USER STATS")
root.geometry("474x266")
root.resizable(False,False)
fg=PhotoImage(file="C:/Users/fayz/Desktop/G1.png")
fg_img=Label(root,image=fg).place(x=0,y=0,relwidth=1,relheight=1)
global Username1
global Password1
Username1 = Entry(root, width=30,bd=5,font=('Times New Roman',10,'bold'))
Username1.place(x=140,y=160)
Username1.insert(0,' Enter Username')
Username1.bind("<FocusIn>",on_enterU)
Username1.bind("<FocusOut>",on_leaveU)

Password1 = Entry(root, width=30,bd=5,font=('Times New Roman',10,'bold'))
Password1.place(x=140,y=190)
Password1.insert(0,' Enter Password')
Password1.bind("<FocusIn>",on_enterP)
Password1.bind("<FocusOut>",on_leaveP)
frame1=Frame(root,width=30,height=2)
frame1.place(x=190,y=160)

login_button=Button(root,text='Login',command=login,bg='firebrick1',cursor='hand2').place (x=220,y=235)

root.mainloop()
