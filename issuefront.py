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
    os.system("python issue(library).py")
def run1():
    os.system("python issueteacher(library).py")
    


top=Tk()
top.title("LIBRARY")
top.geometry("500x350")

front=Label(top,text="ISSUE BOOK FORM",font='Helvetica 20 bold',bg='lightpink')
front.pack()
student=Button(top,text="STUDENT",font='Helvetica 17 bold',command=run,activebackground='red',foreground='green')
student.place(x=100,y=100)
teacher=Button(top,text="TEACHER",font='Helvetica 17 bold',command=run1,activebackground='red',foreground='green')
teacher.place(x=250,y=100)
top.resizable(0,0)
top.mainloop()