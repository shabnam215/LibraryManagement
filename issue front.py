# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:07:59 2024

@author: INDIA
"""

import os
import sys
from tkinter import *
from tkinter import ttk
import mysql.connector
def run():
    os.system("student.py")
    


top=Tk()
top.title("LIBRARY")
top.geometry("500x350")

front=Label(top,text="ISSUE BOOK FORM",font='Helvetica 20 bold')
front.pack()
student=Button(top,text="STUDENT",font='Helvetica 17 bold')
student.pack(anchor="center",side=TOP)
#student.place(x=600,y=50)
teacher=Button(top,text="TEACHER",font='Helvetica 17 bold')
#teacher.place(x=600,y=100)
teacher.pack(anchor="center", side=TOP)
top.mainloop()