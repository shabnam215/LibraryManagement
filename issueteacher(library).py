# -*- coding: utf-8 -*-
"""
Created on Thu May 30 04:09:17 2024

@author: INDIA
"""

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
cursor=mydb.cursor()
bid=[]
brid=[]
def reading():
    cursor.execute("select ID from teacher");
    d=cursor.fetchall()
    for i in d:
        bid.append(i[0])
    mydb.commit()
def stu():
    cc=mydb.cursor()
    cc.execute("select ID from teacher");
    d1=cc.fetchall()
    for i in d1:            
        brid.append(i[0])
    mydb.commit()
def dt():
    cc1=mydb.cursor()
    e0=ebook.get()
    e1=ebor.get()
    e2=esid.get_date()
    print(e2)
    val=(e0,e1,e2,'TEACHER','YES')
    cc1.execute("insert into issuereturn (BOOKID,BORRID,ISSUEDATE,CATEGORY,STAT) values(%s,%s,'%s','%s','%s')"%val);    
    mydb.commit()
def clear():
    ebook.delete(0,END)
    ebor.delete(0,END)
    eisd.delete(0,END)    
    mydb.commit()


from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar

reading()
stu()

top=Tk()
top.title("LIBRARY")
top.geometry("600x400")
front=Label(top,text="ISSUE BOOK",font='Helvetica 25 bold',bg='lightpink')
front.grid(row=0,column=2)
book=Label(top,text="BOOK ID", font='Times  10 bold').grid(row=2,column=1)
ebook=ttk.Combobox(top,values=bid)
ebook.grid(row=2,column=2)
bor=Label(top,text="BORROWER ID", font='Times  10 bold').grid(row=3,column=1)
ebor=ttk.Combobox(top,values=brid)
ebor.grid(row=3,column=2)
isd=Label(top,text="ISSUE DATE", font='Times  10 bold').grid(row=4,column=1)
esid=Calendar(top,selectmode='day', year=2024, month=5, day=30,date_pattern="yyyy-mm-dd")
esid.grid(row=4,column=2)
issue=Button(top,text="ISSUED",command=dt,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=80,y=330)
clr=Button(top,text="CLEAR",command=clear,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=300,y=330)
top.resizable(0,0)
top.mainloop()


