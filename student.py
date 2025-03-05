# -*- coding: utf-8 -*-
"""
Created on Mon May 27 03:15:17 2024

@author: INDIA
"""
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
cursor=mydb.cursor()
from tkinter import *
from tkinter import ttk
def adds():
    val=(eid.get(),ename.get(),ecourse.get(),econtact.get())
    cursor.execute("insert into student(ID,NAME,COURSE,CONTACTNUMBER) values(%s,'%s','%s','%s')"%val);
    mydb.commit()
def searchs():    
    shid=eid.get()
    cc=mydb.cursor()
    cc.execute("select * from student where ID=%s"%shid)
    d=cc.fetchall()
    ename.insert(END,d[0][1])
    if(d[0][2]=="1"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="2"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="3"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="4"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="5"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="6"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="7"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="8"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="9"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="10"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="11"):        
        ecourse.set(d[0][2])
    elif(d[0][2]=="12"):        
        ecourse.set(d[0][2])
    econtact.insert(END,d[0][3])
def updates():
    e0=eid.get()
    e1=ename.get()
    e2=ecourse.get()
    e3=econtact.get()
    val1=e1,e2,e3,e0
    cc1=mydb.cursor()
    cc1.execute("update student set SNAME='%s', COURSE='%s', CONTACTNUMBER='%s' where id=%s "%val1);
    #cc1.execute("update student set NAME='sandeep', COURSE='10', CONTACTNUMBER='122556346265'");
    mydb.commit()
def clr():
    eid.delete(0,"end")    
    ename.delete(0,"end")    
    ecourse.delete(0,"end") 
    econtact.delete(0,"end")
    
    
    
    
    
    
    
top=Tk()
top.title("LIBRARY")
top.geometry("650x350")
front=Label(top,text="STUDENT DETAIL",font='Helvetica 25 bold',bg='lightpink').grid(row=0,column=2)
ids=Label(top,text="ID", font='Times  10 bold').grid(row=1,column=1)
eid=Entry(top)
eid.grid(row=1,column=2)
sname=Label(top,text="NAME", font='Times  10 bold').grid(row=2,column=1)
ename=Entry(top)
ename.grid(row=2,column=2)
course=Label(top,text="CLASS", font='Times  10 bold').grid(row=3,column=1)
ecourse=ttk.Combobox(top,value=["1","2","3","4","5","6","7","8","9","10","11","12"])
ecourse.grid(row=3,column=2)
contact=Label(top,text="CONTACT NUMBER", font='Times  10 bold').grid(row=4,column=1)
econtact=Entry(top)
econtact.grid(row=4,column=2)
add=Button(top,text="ADD",command=adds,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=30,y=150)
update=Button(top,text="UPDATE",command=updates,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=260,y=150)
search=Button(top,text="SEARCH",command=searchs,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=30,y=200)
clear=Button(top,text="CLEAR", command=clr,font='Helvetica 15 bold',activebackground='red',foreground='green').place(x=260,y=200)
top.resizable(0,0)
top.mainloop()


