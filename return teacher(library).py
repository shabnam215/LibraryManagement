# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:19:42 2024

@author: INDIA
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 29 03:44:19 2024

@author: INDIA
"""
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="library")
cursor=mydb.cursor()
from tkinter import *
from datetime import timedelta,datetime
from tkcalendar import Calendar
from tkinter import ttk

fine=0
bid=[]
brid=[]
def reads():
    cursor.execute("select BOOKID from issuereturn");
    d=cursor.fetchall()
    for i in d:
        bid.append(i[0])
    mydb.commit()
def stu():
    cc=mydb.cursor()
    cc.execute("select BORRID from issuereturn");
    d1=cc.fetchall()
    for i in d1:            
        brid.append(i[0])
    mydb.commit()
def reading():
    ee=int(ebook.get())
    ee1=int(eborr.get())
    act=eard.get_date()
    act1=datetime.strptime(act,'%Y-%m-%d').date()

    #val=(ee,ee1,"STUDENT","YES")
    val=(ee,ee1)
    cc1=mydb.cursor()
    cc1.execute("select * from issuereturn where BOOKID='%s'AND BORRID='%s'AND CATEGORY='TEACHER' AND STAT='YES'"%val);
    d=cc1.fetchall()
    for i in d:
        print(i)
    dd1=datetime.strptime(act,'%Y-%m-%d').date()
    dd2=datetime.strptime(str(i[3]),'%Y-%m-%d').date()
    diff=dd1-dd2
    da=(diff.days)
    if(da>0):
        Fine=da*10
        cc2=mydb.cursor()
        val1=(act1,Fine,ee,ee1)
        cc2.execute("update issuereturn set actualReturnDate='%s', fine=%s where BOOKID=%s AND BORRID=%s AND CATEGORY='TEACHER' AND STAT='YES'"%val1);
    else:
        cc2=mydb.cursor()
        val1=(act1,0,ee,ee1)
        cc2.execute("update issuereturn set actualReturnDate='%s', fine=%s where BOOKID=%s AND BORRID=%s AND CATEGORY='TEACHER' AND STAT='YES'"%val1);
    mydb.commit() 
                
           
            
        
reads()
stu()
top=Tk()

info=StringVar()

top.title("LIBRARY")
top.geometry("500x350")
#front=Label(top,text="RETURN BOOK").grid(row=0,column=2)
book=Label(top,text="BOOK ID").grid(row=1,column=1)
ebook=ttk.Combobox(top,values=bid)
ebook.grid(row=1,column=2)
borr=Label(top,text="BORROWER ID").grid(row=2,column=1)
eborr=ttk.Combobox(top,values=brid)
eborr.grid(row=2,column=2)
ard=Label(top,text="ACTUAL RETURN DATE").grid(row=4,column=1)
eard=Calendar(top,selectmode='day', year=2024, month=5, day=30,date_pattern="yyyy-mm-dd")
eard.grid(row=4,column=2)
fine=Label(top,text="FINE").grid(row=10,column=1)
efine=Entry(top)
efine.grid(row=10,column=2)
bb=Button(top,text="return",command=reading)
bb.grid(row=15,column=1)
top.mainloop()