# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:14:05 2024

@author: INDIA
"""
import os
import sys
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="library")
cursor=mydb.cursor()
def logg():
    t=0
    l1=elogin.get()
    l2=epassw.get()
    val=(l1,l2)
    cursor.execute("select * from admin where login='%s' and passwords='%s'"%val);
    d=cursor.fetchall()
    for i in d:
        print(i)
        if(i[0]==l1 and i[1]==l2):
            os.system("python FRONT(LIBRARY).py")
            t=t+1
    if(t==0):
        messagebox.showinfo("LIBRARY","WRONG LOGIN AND PASSWORD")
        
    
def clr():
    elogin.delete(0,END)
    epassw.delete(0,END)

top=Tk()
top.title("LIBRARY")
top.geometry("400x350")
front=Label(top,text="LOGIN",font='Helvetica 25 bold').place(x=150,y=10)
login=Label(top,text="LOGIN ID",font='Helvetica 15 bold').place(x=30,y=50)
elogin=Entry(top)
elogin.place(x=150,y=50)
passw=Label(top,text="PASSWORD",font='Helvetica 15 bold').place(x=30,y=100)
epassw=Entry(top)
epassw.place(x=150,y=100)
log=Button(top,text="LOGIN",command=logg,font='Helvetica 15 bold').place(x=100,y=150)
clear=Button(top,text="CLEAR",command=clr,font='Helvetica 15 bold').place(x=200,y=150)
top.resizable(0,0)
top.mainloop()
