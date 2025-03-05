# -*- coding: utf-8 -*-
"""
Created on Wed May 29 03:27:45 2024

@author: INDIA
"""

from tkinter import *

top=Tk()
top.title("ISSUE AND RETURN")
top.geometry("400x250")
front=Label(top,text="LIBRARY")
front.grid(row=0,column=2)
book=Label(top,text="BOOK ID").grid(row=1,column=1)
ebook=Entry(top)
ebook.grid(row=1,column=2)
bor=Label(top,text="BORROWER ID").grid(row=2,column=1)
ebor=Entry(top)
ebor.grid(row=2,column=2)
isd=Label(top,text="ISSUE DATE").grid(row=3,column=1)
eisd=Entry(top)
eisd.grid(row=3,column=2)
erd=Label(top,text="EXPECTED RETURN DATE").grid(row=4,column=1)
eerd=Entry(top)
eerd.grid(row=4,column=2)
ard=Label(top,text="ACTUAL RETURN DATE").grid(row=5,column=1)
eard=Entry(top)
eard.grid(row=5,column=2)
fine=Label(top,text="FINE").grid(row=6,column=1)
efine=Entry(top)
efine.grid(row=6,column=2)
