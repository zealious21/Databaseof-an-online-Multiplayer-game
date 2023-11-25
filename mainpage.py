import tkinter
from tkinter import *
import mysql.connector
import tkinter.messagebox
from tkinter import  ttk

from tkinter import messagebox
def textdisplay():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e1.focus_set()
    Refreshf()
    show()


def Search():
    root.destroy()
    import search
def read():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dbnbg3jt@",
        database="master")
    mycursor = conn.cursor()
    mycursor.execute("Select * from gamestats;")
    results=mycursor.fetchall()
    conn.commit()
    conn.close()
    return results

def Refresh():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")

    my_tree.tag_configure('orow')

def Refreshf():
    for data in my_tree.get_children():
        my_tree.delete(data)



    my_tree.tag_configure('orow')
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    row_id=my_tree.selection()[0]
    select=my_tree.set(row_id)
    e1.insert(0,select['PID'])
    e2.insert(0, select['PLAYER NAME'])
    e3.insert(0, select['AGE'])
    e4.insert(0, select['COUNTRY'])
    e5.insert(0, select['EXP-LEVEL'])
    e6.insert(0, select['KILLS'])
    e7.insert(0, select['GAMES'])
def Logout():
    root.destroy()
    import main
def insert():

    PID=e1.get()
    PNAME=e2.get()
    AGE=e3.get()
    COUNTRY=e4.get()
    EXPLEVEL=e5.get()
    KILLS=e6.get()
    Games=e7.get()




    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dbnbg3jt@",
        database="master")
    mycursor = conn.cursor()

    if(PID=="" or PNAME=="" or AGE=="" or COUNTRY=="" or EXPLEVEL=="" or KILLS=="" or Games==""):
        messagebox.showerror("ERROR", "ENTER ALL DATA TO INSERT")




    else:
        try:
           add="INSERT into gamestats (PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES) values(%s,%s,%s,%s,%s,%s,%s);"
           VAL=(PID,PNAME,AGE,COUNTRY,EXPLEVEL,KILLS,Games)
           mycursor.execute(add,VAL)
           conn.commit()
           lastid=mycursor.lastrowid
           messagebox.showinfo("INFORMATION","Data inserted")
           e1.delete(0,END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e5.delete(0, END)
           e6.delete(0, END)
           e7.delete(0, END)
           e1.focus_set()

        except Exception as e:
          print(e)
          conn.rollback()
          conn.close
    Refresh()
def update():

    PID=e1.get()
    PNAME=e2.get()
    AGE=e3.get()
    COUNTRY=e4.get()
    EXPLEVEL=e5.get()
    KILLS=e6.get()
    Games=e7.get()
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dbnbg3jt@",
        database="master")
    mycursor = conn.cursor()

    if (PID == ""):
        messagebox.showerror("ERROR", "ENTER PLAYER ID TO UPDATE")

    #elif(  PNAME=="" or AGE=="" or COUNTRY=="" or EXPLEVEL=="" or KILLS=="" or Games==""):
    #    messagebox.showerror("ERROR", "ENTER ALL DATA TO UPDATE")


    else:
        if(PID!="" and PNAME!="" and AGE!="" and COUNTRY!="" and EXPLEVEL!="" and KILLS!="" and Games!=""):
            try:
                ADD = "UPDATE gamestats set PLAYERNAME=%s,AGE=%s,COUNTRY=%s,EXPLEVEL=%s,KILLS=%s,GAMES=%s where PLAYERID=%s;"
                VAL = (PNAME, AGE, COUNTRY, EXPLEVEL, KILLS, Games, PID)
                mycursor.execute(ADD, VAL)
                conn.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("INFORMATION", "Data UPDATED SUCCESSFULLY")
                textdisplay()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close
        elif (PID != "" and PNAME != "" and AGE != "" and COUNTRY != "" and EXPLEVEL != ""and KILLS!=""):
            try:
                ADD = "UPDATE gamestats set PLAYERNAME=%s,AGE=%s,COUNTRY=%s,EXPLEVEL=%s,KILLS=%s where PLAYERID=%s;"
                VAL = (PNAME, AGE, COUNTRY, EXPLEVEL,KILLS, PID)
                mycursor.execute(ADD, VAL)
                conn.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("INFORMATION", "Data UPDATED SUCCESSFULLY")
                textdisplay()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close
        elif (PID != "" and PNAME != "" and AGE != "" and COUNTRY!=""and EXPLEVEL!=""):
            try:
                ADD = "UPDATE gamestats set PLAYERNAME=%s,AGE=%s,COUNTRY=%s,EXPLEVEL=%s where PLAYERID=%s;"
                VAL = (PNAME, AGE,COUNTRY,EXPLEVEL, PID)
                mycursor.execute(ADD, VAL)
                conn.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("INFORMATION", "Data UPDATED SUCCESSFULLY")
                textdisplay()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close
        elif (PID != "" and PNAME != "" and AGE != "" and COUNTRY!=""):
            try:
                ADD = "UPDATE gamestats set PLAYERNAME=%s,AGE=%s,COUNTRY=%s where PLAYERID=%s;"
                VAL = (PNAME, AGE,COUNTRY, PID)
                mycursor.execute(ADD, VAL)
                conn.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("INFORMATION", "Data UPDATED SUCCESSFULLY")
                textdisplay()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close
        elif (PID != "" and PNAME != "" and AGE != ""):
            try:
                ADD = "UPDATE gamestats set PLAYERNAME=%s,AGE=%s where PLAYERID=%s;"
                VAL = (PNAME, AGE, PID)
                mycursor.execute(ADD, VAL)
                conn.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("INFORMATION", "Data UPDATED SUCCESSFULLY")
                textdisplay()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close
        elif (e1.get != "" and e2.get() != ""):
            try:
                ADD = "UPDATE gamestats set PLAYERNAME=%s where PLAYERID=%s;"
                VAL = (PNAME, PID)
                mycursor.execute(ADD, VAL)
                conn.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("INFORMATION", "Data UPDATED SUCCESSFULLY")
                textdisplay()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close

        else:
            print(12)






















def delete():
    PID=e1.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dbnbg3jt@",
        database="master")
    mycursor = conn.cursor()

    if(PID=="" ):
        messagebox.showerror("ERROR", "ENTER PLAYERID TO DELETE")


    else:
        try:
           add="DELETE from gamestats where PLAYERID=%s;"
           VAL=(PID,)
           mycursor.execute(add,VAL)
           conn.commit()
           lastid=mycursor.lastrowid
           messagebox.showinfo("INFORMATION","Data DELETED SUCCESSFULLY")
           e1.delete(0,END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e5.delete(0, END)
           e6.delete(0, END)
           e7.delete(0, END)
           e1.focus_set()

        except Exception as e:
          print(e)
          conn.rollback()
          conn.close
    Refresh()
def show():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dbnbg3jt@",
        database="master")
    mycursor = conn.cursor()
    mycursor.execute("SELECT PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES FROM gamestats;")
    records=mycursor.fetchall()
    print(records)

    for i, (PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES) in enumerate(records,start=1):
        my_tree.insert("","end", values=(PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES))
        conn.close
root=Tk()
root.title("Mainpage")
root.geometry("1125x660")
root.resizable(False,False)
fgm=PhotoImage(file="C:/Users/fayz/Desktop/for_auto_x2 (2).png")
fg_img=Label(root,image=fgm).place(x=0,y=-130,relwidth=1,relheight=1)

global e1
global e2
global e3
global e4
global e5
global e6
global e7

#photo=PhotoImage(file='image.png')
#label12=Label(root,image=photo).grid(row=8,column=5)
label1=Label(root,text="PLAYER ID",width=20,height=2,bg="pink").grid(row=0,column=0)
label2=Label(root,text="PLAYER NAME",width=20,height=2,bg="pink").grid(row=1,column=0)
label3=Label(root,text="AGE",width=20,height=2,bg="pink").grid(row=2,column=0)
label4=Label(root,text="COUNTRY",width=20,height=2,bg="pink").grid(row=3,column=0)
label5=Label(root,text="EXPLEVEL",width=20,height=2,bg="pink").grid(row=4,column=0)
label6=Label(root,text="KILLS",width=20,height=2,bg="pink").grid(row=5,column=0)
label7=Label(root,text="GAMES",width=20,height=2,bg="pink").grid(row=6,column=0)

e1=Entry(root,width=30,borderwidth=8)
e1.grid(row=0,column=1)
e2=Entry(root,width=30,borderwidth=8)
e2.grid(row=1,column=1)
e3=Entry(root,width=30,borderwidth=8)
e3.grid(row=2,column=1)
e4=Entry(root,width=30,borderwidth=8)
e4.grid(row=3,column=1)
e5=Entry(root,width=30,borderwidth=8)
e5.grid(row=4,column=1)
e6=Entry(root,width=30,borderwidth=8)
e6.grid(row=5,column=1)
e7=Entry(root,width=30,borderwidth=8)
e7.grid(row=6,column=1)


scrollbarx=Scrollbar(root,orient=HORIZONTAL)
scrollbary=Scrollbar(root,orient=VERTICAL)
my_tree=ttk.Treeview(root)
my_tree.place(x=-100,y=300,height=344,width=1203,relx=0)
my_tree.configure(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
my_tree.configure(selectmode="extended")

scrollbarx.configure(command=my_tree.xview)
scrollbary.configure(command=my_tree.yview)
scrollbarx.place(width=1500,height=22,relx=0,rely=0.975)
scrollbary.place(relx=0.98,rely=0.455,width=22,height=368)

my_tree.configure(
    columns=("PID","PLAYER NAME","AGE","COUNTRY","EXP-LEVEL","KILLS","GAMES","K/G RATIO")
)
my_tree.heading("PID",text="PID",anchor=W)
my_tree.heading("PLAYER NAME",text="PLAYER NAME",anchor=W)
my_tree.heading("AGE",text="AGE",anchor=W)
my_tree.heading("COUNTRY",text="COUNTRY",anchor=W)
my_tree.heading("EXP-LEVEL",text="EXP-LEVEL",anchor=W)
my_tree.heading("KILLS",text="KILLS",anchor=W)
my_tree.heading("GAMES",text="GAMES",anchor=W)
#my_tree.heading("K/G RATIO",text="K/G RATIO",anchor=W)


addBTn=Button(root,text="ADD",width=10,height=1,bd=5,font=('Arial',15),command=insert,cursor='hand2').place(x=0,y=253)
updateBTn=Button(root,text="UPDATE",width=10,height=1,bd=5,font=('Arial',15),command=update,cursor='hand2').place(x=170,y=253)
deleteBTn=Button(root,text="DELETE",width=10,height=1,bd=5,font=('Arial',15),command=delete,cursor='hand2').place(x=340,y=253)
SearchBTn=Button(root,text="Search",width=10,height=1,bd=5,font=('Arial',15),command=Search,cursor='hand2').place(x=510,y=253)

LogOutBTn=Button(root,text="Logout",width=10,height=1,bd=5,font=('Arial',15),command=Logout,cursor='hand2').place(x=680,y=253)

show()
my_tree.bind('<Double-Button-1>',GetValue)
root.mainloop()


