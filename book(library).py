# -*- coding: utf-8 -*-
"""
Created on Tue May 28 04:33:18 2024

@author: INDIA
""" 
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
cursor=mydb.cursor()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def adds():
    val=(bid.get(),bname.get(),subject.get(),bpub.get(),baut.get(),bprice.get())
    cursor.execute("insert into book(BID,BNAME,BSUB,BPUB,BAUT,BPRICE) values(%s,'%s','%s','%s','%s','%s')"%val);
    mydb.commit()
    messagebox.showinfo("HELLO","RECORD ADDED")
def searchs():
    bsrch=bid.get()
    cc=mydb.cursor()
    cc.execute("select * from book where BID=%s"%bsrch)
    d=cc.fetchall()
    for i in d:
        print(i)
    bname.insert(END,d[0][1])
    if(d[0][2]=="ENGLISH"):        
        subject.set(d[0][2])
    elif(d[0][2]=="MATHEMATICS"):        
        subject.set(d[0][2])
    elif(d[0][2]=="SCIENCE"):        
        subject.set(d[0][2])
    elif(d[0][2]=="SOCIAL SCIENCE"):        
        subject.set(d[0][2])
    elif(d[0][2]=="PUNJABI"):        
        subject.set(d[0][2])
    elif(d[0][2]=="HINDI"):        
        subject.set(d[0][2])
    elif(d[0][2]=="COMPUTER SCIENCE/IT"):        
        subject.set(d[0][2])
    elif(d[0][2]=="EVS"):        
        subject.set(d[0][2])
    elif(d[0][2]=="PHYSICAL EDUCATION"):        
        subject.set(d[0][2])
    bpub.insert(END,d[0][3])
    baut.insert(END,d[0][4])
    bprice.insert(END,d[0][5])
def updates():
    e0=bid.get()
    e1=bname.get()
    e2=subject.get()
    e3=bpub.get()
    e4=baut.get()
    e5=bprice.get()
    val1=(e1,e2,e3,e4,e5,e0)
    cc1=mydb.cursor()
    cc1.execute("update book set  BNAME='%s', BSUB='%s', BPUB='%s', BAUT='%s', BPRICE='%s' where BID=%s" %val1);
    mydb.commit()
    messagebox.showinfo("HELLO","RECORD UPDATED")
def deletes():
    e0=bid.get()  
    cc2=mydb.cursor()
    cc2.execute("delete from book where BID=%s" %e0);
    mydb.commit()
    messagebox.showinfo("HELLO","RECORD DELETED")
def clr():
    bid.delete(0,END)
    bname.delete(0,END)
    subject.delete(0,END)
    bpub.delete(0,END)
    baut.delete(0,END)
    bprice.delete(0,END)

top=Tk()
top.title("LIBRARY")
top.geometry("600x400")
front=Label(top,text="BOOK DETAIL",bg='lightpink',font='Helvetica 25 bold').grid(row=0,column=2)
ids=Label(top,text="BOOK ID", font='Times  10 bold').grid(row=1,column=1)
bid=Entry(top)
bid.grid(row=1,column=2)
sname=Label(top,text="BOOK NAME", font='Times  10 bold').grid(row=2,column=1)
bname=Entry(top)
bname.grid(row=2,column=2)
sub=Label(top,text="SUBJECT", font='Times  10 bold').grid(row=3,column=1)
subject=ttk.Combobox(top,values=["ENGLISH","MATHEMATICS","SCIENCE","SOCIAL SCIENCE","PUNJABI","HINDI","COMPUTER SCIENCE/IT","EVS","PHYSICAL EDUCATION"])
subject.grid(row=3,column=2)
pub=Label(top,text="PUBLISHER NAME", font='Times  10 bold').grid(row=4,column=1)
bpub=Entry(top)
bpub.grid(row=4,column=2)
aut=Label(top,text="AUTHOR NAME", font='Times  10 bold').grid(row=5,column=1)
baut=Entry(top)
baut.grid(row=5,column=2)
price=Label(top,text="PRICE", font='Times  10 bold').grid(row=6,column=1)
bprice=Entry(top)
bprice.grid(row=6,column=2)
add=Button(top,text="ADD NEW BOOK",command=adds,activebackground='red',foreground='green',font='Helvetica 15 bold').place(x=30,y=180)
update=Button(top,text="UPDATE BOOK DETAIL",command=updates,activebackground='red',foreground='green',font='Helvetica 15 bold').place(x=260,y=180)
search=Button(top,text="SEARCH BOOK",command=searchs,activebackground='red',foreground='green',font='Helvetica 15 bold').place(x=30,y=230)
delete=Button(top,text="DELETE BOOK",command=deletes,activebackground='red',foreground='green',font='Helvetica 15 bold').place(x=260,y=230)
clear=Button(top,text="CLEAR", command=clr,activebackground='red',foreground='green',font='Helvetica 15 bold').place(x=200,y=280)
top.resizable(0,0)
top.mainloop()



