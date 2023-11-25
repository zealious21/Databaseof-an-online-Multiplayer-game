from tkinter import *
import mysql.connector
import tkinter.messagebox
from tkinter import  ttk
from tkinter import messagebox
from PIL import Image, ImageTk
def back():
    root.destroy()
    import mainpage
    root.mainloop()
def Refresh():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")

    my_tree.tag_configure('orow')
#def show():
#     conn = mysql.connector.connect(
  #      host="localhost",
 #       user="root",
  #      password="dbnbg3jt@",
#        database="master")
 #   mycursor = conn.cursor()
 #   mycursor.execute("SELECT PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES FROM gamestats;")
 #   records=mycursor.fetchall()
 #   print(records)

 #   for i, (PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES) in enumerate(records,start=1):
  #      my_tree.insert("","end", values=(PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES))
 #      conn.close
def show():


    if (select.get()=='PID'):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        mycursor.execute("SELECT PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES FROM gamestats Order by PLAYERID;")
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close



    elif(select.get() == 'PLAYER NAME'):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        mycursor.execute("SELECT PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES FROM gamestats Order by PLAYERNAME;")
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close()



    elif (select.get() == 'AGE'):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        mycursor.execute("SELECT PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES FROM gamestats Order by AGE;")
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close


    elif (select.get() == 'COUNTRY'):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        mycursor.execute("SELECT PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES FROM gamestats Order by COUNTRY;")
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close


    elif (select.get() == 'EXPLEVEL'):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        mycursor.execute("SELECT PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES FROM gamestats Order by EXPLEVEL;")
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close

    elif (select.get() == 'GAMES'):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        mycursor.execute("SELECT PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES FROM gamestats Order by GAMES;")
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close


    elif (select.get() == 'KILLS'):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        mycursor.execute("SELECT PLAYERID,PLAYERNAME,AGE,COUNTRY,EXPLEVEL,KILLS,GAMES FROM gamestats Order by KILLS;")
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close


    elif (select.get() == 'Enter column for search'):
        messagebox.showinfo("ENTER", "PLEASE ENTER COLUMN FOR SEARCH")

    else:
        messagebox.showerror("ERROR", "ENTER COLUMN FOR SEARCH")
    impo=e8.get()
    if(e8.get()==''):
        print(12)

    elif(select.get()=='PID' and e8.get!=''):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        ADD = "select * from gamestats  where PLAYERID=%s;"
        VAL = (impo)
        mycursor.execute(ADD,( VAL,))

        lastid = mycursor.lastrowid
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close

    elif (select.get() == 'PLAYER NAME' and e8.get != ''):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        ADD = "select * from gamestats  where PLAYERNAME=%s;"
        VAL = (impo)
        mycursor.execute(ADD, (VAL,))

        lastid = mycursor.lastrowid
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close

    elif (select.get() == 'AGE' and e8.get != ''):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        ADD = "select * from gamestats  where AGE=%s;"
        VAL = (impo)
        mycursor.execute(ADD, (VAL,))

        lastid = mycursor.lastrowid
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close

    elif (select.get() == 'COUNTRY' and e8.get != ''):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        ADD = "select * from gamestats  where COUNTRY=%s;"
        VAL = (impo)
        mycursor.execute(ADD, (VAL,))

        lastid = mycursor.lastrowid
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close

    elif (select.get() == 'EXPLEVEL' and e8.get != ''):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        ADD = "select * from gamestats  where EXPLEVEL=%s;"
        VAL = (impo)
        mycursor.execute(ADD, (VAL,))

        lastid = mycursor.lastrowid
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close

    elif (select.get() == 'KILLS' and e8.get != ''):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        ADD = "select * from gamestats  where KILLS=%s;"
        VAL = (impo)
        mycursor.execute(ADD, (VAL,))

        lastid = mycursor.lastrowid
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close
    elif (select.get() == 'GAMES' and e8.get != ''):
        Refresh()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbnbg3jt@",
            database="master")
        mycursor = conn.cursor()
        ADD = "select * from gamestats  where GAMES=%s;"
        VAL = (impo)
        mycursor.execute(ADD, (VAL,))

        lastid = mycursor.lastrowid
        records = mycursor.fetchall()
        print(records)

        for i, (PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES) in enumerate(records, start=1):
            my_tree.insert("", "end", values=(PLAYERID, PLAYERNAME, AGE, COUNTRY, EXPLEVEL, KILLS, GAMES))
            conn.close
    else:
        print(12)









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

   # for array in read():
  #      my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")

  #  my_tree.tag_configure('orow')

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
    e2.insert(0, select['PNAME'])
    e3.insert(0, select['AGE'])
    e4.insert(0, select['COUNTRY'])
    e5.insert(0, select['EXPLEVEL'])
    e6.insert(0, select['KILLS'])
    e7.insert(0, select['GAMES'])

root=Tk()
root.title("Searchpage")
root.geometry("1125x660")
root.resizable(False,False)
fm=PhotoImage(file="C:/Users/fayz/Desktop/bgmm (2) (1) (1).png")
fg_img=Label(root,image=fm).place(x=0,y=-130,relwidth=1,relheight=1)
e8=Entry(root,width=30,borderwidth=8)
e8.place(x=650,y=270)
select=ttk.Combobox(root,width=25,font='Courier',values=("PID","PLAYER NAME","AGE","COUNTRY","EXPLEVEL","KILLS","GAMES"))
select.place(x=235,y=277)
select.set("Enter column for search")
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
show()
Refresh()
my_tree.bind('<Double-Button-1>',GetValue)
backBTn=Button(root,text="BACK",width=10,height=1,bd=5,font=('Arial',15),command=back,cursor='hand2').place(x=0,y=253)


SearchBTn=Button(root,text="Search",width=10,height=1,bd=5,font=('Arial',15),command=show,cursor='hand2').place(x=510,y=253)
root.mainloop()
