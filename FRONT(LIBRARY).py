# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:24:47 2024

@author: INDIA
"""
import os
import sys
from tkinter import *
from tkinter import ttk
import mysql.connector
def run():
    os.system("python student.py")
def run1():
    os.system("python teacher(library).py")
def run2():
    os.system("python issuefront.py")
def run3():
    os.system("python returnfront.py")
def run4():
    os.system("python reportfront.py")
    
top=Tk()
top.configure(bg="lightyellow")
top.title("LIBRARY")
top.geometry("650x350")
front=Label(top,text="REGISTRATION FORM",font='Helvetica 25 bold',bg='lightpink')
front.place(x=150,y=5)
student=Button(top,text="STUDENT",command=run,font='Helvetica 15 bold',activebackground='red',foreground='green')
student.place(x=50,y=150)
teacher=Button(top,text="TEACHER",command=run1,font='Helvetica 15 bold',activebackground='red',foreground='green')
teacher.place(x=170,y=150)
issue=Button(top,text="ISSUE",command=run2,font='Helvetica 15 bold',activebackground='red',foreground='green')
issue.place(x=290,y=150)
ret=Button(top,text="RETURN",command=run3,font='Helvetica 15 bold',activebackground='red',foreground='green')
ret.place(x=380,y=150)
rep=Button(top,text="REPORT",command=run4,font='Helvetica 15 bold',activebackground='red',foreground='green')
rep.place(x=500,y=150)
top.resizable(0,0)
top.mainloop()
