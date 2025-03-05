# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:09:09 2024

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
front=Label(top,text="RETURN BOOK FORM",font='Helvetica 25 bold')
front.pack()
student=Button(top,text="STUDENT",font='Helvetica 17 bold')
student.pack(anchor="center")
teacher=Button(top,text="TEACHER",font='Helvetica 17 bold')
teacher.pack(anchor="center")
top.mainloop()

