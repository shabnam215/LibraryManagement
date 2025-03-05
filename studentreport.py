# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:39:37 2024

@author: INDIA
"""

import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="library")
cursor=mydb.cursor()
from tkinter import *
from tkinter import ttk
bk=[]

def search():
    cursor.execute("SELECT * FROM student")
    i=10 
    for student in cursor: 
        for j in range(len(student)):
            e = Entry(top, width=30, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1

top=Tk()

search()
front=Label(top,text="STUDENT DETAIL",bg='lightpink').grid(row=2,column=3)

top.mainloop()
