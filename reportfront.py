# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:44:51 2024

@author: INDIA
"""

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
    os.system("python studentreport.py")
def run1():
    os.system("python teacherreport.py")
def run2():
    os.system("python issuereturnreport.py")
def run3():
    os.system("python reportsubjectwise.py")

    
top=Tk()
top.title("LIBRARY")
top.geometry("500x350")
front=Label(top,text="REPORT",font='Helvetica 25 bold',bg='lightpink')
front.pack()
student=Button(top,text="STUDENT",command=run,font='Helvetica 15 bold',activebackground='red',foreground='green')
student.place(x=200,y=60)
teacher=Button(top,text="TEACHER",command=run1,font='Helvetica 15 bold',activebackground='red',foreground='green')
teacher.place(x=200,y=120)
issue=Button(top,text="FINE",command=run2,font='Helvetica  15 bold',activebackground='red',foreground='green')
issue.place(x=230,y=180)
issue=Button(top,text="SUBJECT WISE REPORT",command=run3,font='Helvetica 15 bold',activebackground='red',foreground='green')
issue.place(x=160,y=240)
top.resizable(0,0)
top.mainloop()
