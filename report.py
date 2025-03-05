# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:10:37 2024

@author: INDIA
"""

import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="library")
cursor=mydb.cursor()
from tkinter import *
from tkinter import ttk
bk=[]
def reads():
    cursor.execute("select DISTINCT(BSUB) from book");
    d=cursor.fetchall()
    for i in d:
        bk.append(i)
    mydb.commit()
def search():
    cursor.execute("SELECT * FROM book")
    i=10 
    for student in cursor: 
        for j in range(len(student)):
            e = Entry(top, width=30, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1

reads()
top=Tk()
book=Label(top,text="SUBJECT").grid(row=2,column=2)
ebook=ttk.Combobox(top,values=bk)
ebook.grid(row=3,column=3)
search=Button(top,text="SEARCH",command=search)
search.grid(row=4,column=4)
top.mainloop()
