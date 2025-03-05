# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:46:14 2024

@author: INDIA
"""

import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="library")
cursor=mydb.cursor()
from tkinter import *
from tkinter import ttk
def search():
    cursor.execute("select BOOKID,BORRID,ISSUEDATE,EXPECTEDRETURNDATE,actualReturnDate,CATEGORY,fine from issuereturn where fine>0");
    
    i=10 
    for student in cursor: 
        for j in range(len(student)):
            e = Entry(top, width=30, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1



top=Tk()

search()
front=Label(top,text="FINE DETAIL",bg='lightpink').grid(row=2,column=3)

top.mainloop()
