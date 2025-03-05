# -*- coding: utf-8 -*-
"""
Created on Wed May 29 03:27:45 2024

@author: INDIA
"""
import mysql.connector
from datetime import timedelta,datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
cursor=mydb.cursor()
bid=[]
brid=[]
def reading():
    cursor.execute("select BID from book");
    d=cursor.fetchall()
    for i in d:
        bid.append(i[0])
    mydb.commit()
def stu():
    cc=mydb.cursor()
    cc.execute("select ID from student");
    d1=cc.fetchall()
    for i in d1:            
        brid.append(i[0])
    mydb.commit()
def dt():
    cc1=mydb.cursor()
    e0=ebook.get()
    e1=ebor.get()
    e2=esid.get_date()
    #e3=errd.get_date()
    dd=datetime.strptime(e2,'%Y-%m-%d').date()
    
    dd1=dd+timedelta(days=7)
    print(dd1)
    val=(e0,e1,e2,dd1,'STUDENT','YES')
    cc1.execute("insert into issuereturn (BOOKID,BORRID,ISSUEDATE,EXPECTEDRETURNDATE,CATEGORY,STAT) values(%s,%s,'%s','%s','%s','%s')"%val);    
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
top.title("ISSUE")
top.geometry("400x250")
front=Label(top,text="LIBRARY")
front.grid(row=0,column=2)
book=Label(top,text="BOOK ID").grid(row=2,column=1)
ebook=ttk.Combobox(top,values=bid)
ebook.grid(row=2,column=2)
bor=Label(top,text="BORROWER ID").grid(row=3,column=1)
ebor=ttk.Combobox(top,values=brid)
ebor.grid(row=3,column=2)
isd=Label(top,text="ISSUE DATE").grid(row=4,column=1)
esid=Calendar(top,selectmode='day', year=2024, month=5, day=30,date_pattern="yyyy-mm-dd")
esid.grid(row=4,column=2)
rrd=Label(top,text="EXPECTED RETURN DATE").grid(row=5,column=1)
errd=Entry(top)
errd.grid(row=5,column=2)
issue=Button(top,text="ISSUED",command=dt).grid(row=6,column=1)
clr=Button(top,text="CLEAR",command=clear).grid(row=6,column=2)
top.mainloop()


