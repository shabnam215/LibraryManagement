# -*- coding: utf-8 -*-
"""
Created on Tue May 28 03:12:40 2024

@author: INDIA
"""
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
cursor=mydb.cursor()
from tkinter import *
from tkinter import messagebox
def adds():
    val=(eid.get(),ename.get(),equali.get(),econtact.get())
    cursor.execute("insert into teacher(ID,TNAME,TQUAL,TCONTACT) values(%s,'%s','%s','%s')"%val);
    mydb.commit()
    messagebox.showinfo("Hi","Record added")
def searchs():
    tid=eid.get()
    cc=mydb.cursor()
    cc.execute("select * from teacher where ID=%s"%tid)
    d=cc.fetchall()
    for i in d:
        print(i)
    ename.insert(END,d[0][1])
    equali.insert(END,d[0][2])
    econtact.insert(END,d[0][3])
    mydb.commit()
def updates():
    e0=eid.get()
    e1=ename.get()
    e2=equali.get()
    e3=econtact.get()
    val1=e1,e2,e3,e0
    cc1=mydb.cursor()
    cc1.execute("update teacher set TNAME='%s', TTQUAL='%s', TCONTACT='%s' where ID=%s "%val1);
    mydb.commit()
    messagebox.showinfo("Hi","Record updated")
def clr():
    eid.delete(0,"end")    
    ename.delete(0,"end")    
    equali.delete(0,"end") 
    econtact.delete(0,"end")
    messagebox.showinfo("As you want infomation is cleared")    

    

top=Tk()
top.title("LIBRARY")
top.geometry("600x300")
front=Label(top,text="TEACHER'S DETAIL",font='Helvetica 25 bold',bg='lightpink').grid(row=0,column=2)
ids=Label(top,text="ID", font='Times  10 bold').grid(row=1,column=1)
eid=Entry(top)
eid.grid(row=1,column=2)
sname=Label(top,text="TEACHER NAME", font='Times  10 bold').grid(row=2,column=1)
ename=Entry(top)
ename.grid(row=2,column=2)
qual=Label(top,text="QUALIFICATION", font='Times  10 bold').grid(row=3,column=1)
equali=Entry(top)
equali.grid(row=3,column=2)
contact=Label(top,text="CONTACT NUMBER", font='Times  10 bold').grid(row=4,column=1)
econtact=Entry(top)
econtact.grid(row=4,column=2)
add=Button(top,text="ADD",command=adds,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=30,y=150)
update=Button(top,text="UPDATE",command=updates,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=260,y=150)
search=Button(top,text="SEARCH",command=searchs,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=30,y=200)
clear=Button(top,text="CLEAR", command=clr,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=260,y=200)
top.resizable(0,0)

top.mainloop()



