# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:18:24 2019

@author: Ayham
"""
import sqlite3
from tkinter import *
from tkinter import scrolledtext
from time import strftime 
# =============================================================================
# 



root = Tk() 
root.title('Project3') 

conn = sqlite3.connect('OrgDB.db')
print("Opened database succuessfully")
conn.execute('''CREATE TABLE IF NOT EXISTS Employees
             (EmployeeNumber INT PRIMARY KEY NOT NULL,
             EmployeeName TEXT NOT NULL,
             EmployeeGender TEXT NOT NULL,
             EmployeeNationality TEXT NOT NULL,
             EmployeeDateofBirth TEXT NOT NULL,
             EmployeeAddress TEXT NOT NULL,
             EmployeeDepartment TEXT NOT NULL,
             EmployeeSalary REAL)''')
 
print("Table created")

def record():
    print("EmployeeNumber: ",     eNumber.get())
    print("EmployeeName: ",       eName.get())
    print("EmployeeGender: ",     eGender.get())
    print("EmployeeNationality: ",eNty.get())
    print("EmployeeDateofBirth: ",eDob.get())
    print("EmployeeAddress: ",    eAddress.get())
    print("EmployeeDepartment: ", eDpt.get())
    print("EmployeeSalary: ",     eSalary.get())


    info=(eNumber.get(),eName.get(),eGender.get(),eNty.get(),eDob.get(),eAddress.get(),eDpt.get(),eSalary.get())
    c=conn.cursor()
    
    c.execute("INSERT INTO Employees VALUES (?,?,?,?,?,?,?,?)",info)
    conn.commit()
    print("Data entered successfully!")
    
    
def CreateEmp():
    c=Toplevel(root)
    c.title("Create Employee")
    c.geometry('400x300')
    EmployeeNumber=Label(c,text="EmployeeNumber").grid(row=0,column=0)
    Entry(c,textvariable=eNumber).grid(row=0,column=1)
    EmployeeName=Label(c,text="EmployeeName").grid(row=1,column=0)
    Entry(c,textvariable=eName).grid(row=1,column=1)
    EmployeeGender=Label(c,text="EmployeeGender").grid(row=2,column=0)
    Entry(c,textvariable=eGender).grid(row=2,column=1)
    EmployeeNationality=Label(c,text="EmployeeNationality").grid(row=3,column=0)
    Entry(c,textvariable=eNty).grid(row=3,column=1)
    EmployeeDateofBirth=Label(c,text="EmployeeDateofBirth").grid(row=4,column=0)
    Entry(c,textvariable=eDob).grid(row=4,column=1)
    EmployeeAddress=Label(c,text="EmployeeAddress").grid(row=5,column=0)
    Entry(c,textvariable=eAddress).grid(row=5,column=1)
    EmployeeDepartment=Label(c,text="EmployeeDepartment").grid(row=6,column=0)
    Entry(c,textvariable=eDpt).grid(row=6,column=1)
    EmployeeSalary=Label(c,text="EmployeeSalary").grid(row=7,column=0)
    Entry(c,textvariable=eSalary).grid(row=7,column=1)
    submit=Button(c,text="Submit",command=record).grid(row=8,column=0)
    submit=Button(c,text="Close",command= root.destroy).grid(row=8,column=1)
    
def ShowData():
    cc=Toplevel(root)
    cc.title("Show Employees Data")
    cc.geometry('400x250')
    txt=scrolledtext.ScrolledText(cc,width=40,height=10)
    txt.grid(column=0,row=0)
    c=conn.cursor()
    c.execute("SELECT * FROM Employees")
    for row in c:
        txt.insert(END,row)


    
eNumber=IntVar()
eName=StringVar()
eGender=StringVar()
eNty=StringVar()
eDob=StringVar()
eAddress=StringVar()
eDpt=StringVar()
eSalary=IntVar()

# creating tkinter window  
# Creating Menubar 
menubar = Menu(root)    
# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='Report', command = None) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy)   
# Adding Edit Menu and commands 
employee = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Employees', menu = employee) 
employee.add_command(label ='Add', command = CreateEmp) 
employee.add_command(label ='View', command = ShowData) 

# Adding Help Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='About', command = None) 
# display Menu 
root.config(menu = menubar) 
root.geometry("800x600")
mainloop() 
