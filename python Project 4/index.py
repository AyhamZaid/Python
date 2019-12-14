# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:20:15 2019

@author: Ayham
"""

from flask import Flask,render_template,request
import sqlite3 as sql
app = Flask(__name__)

#---------------------Start Login Function------------------
@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        try:
            name=request.form["name"]
            password=request.form["pass"]
            with sql.connect("Org.db") as con:
                cur = con.cursor()
                cur.execute("select * from login where name = 'Ayham' AND pass = '123456'")
                rows = cur.fetchall()
                if name == rows[0][0] and password == rows[0][1]:
                    msg="Logged in successfully!"
                    return render_template("home.html",name=name,msg=msg)
                else:
                    msg="Try Agian"
                    return render_template("login.html",msg=msg)
                    
        except:
            print("Try agian")
        
        
    elif request.method == "GET":
       return render_template("home.html")
   
    
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        msg="try agian"
        return render_template("login.html",msg=msg)
    elif request.method=="GET":
        return render_template("login.html")

#---------------------End Login Function------------------
        
    
    
#---------------------Start Add Department Function-------
    

@app.route("/adddepartment",methods=["POST","GET"])
def add_department():
    try:
        with sql.connect("Org.db") as con:
            cur = con.cursor()
            cur.execute("select * from locations")
            rows = cur.fetchall()
    except:
         print("Try agian")
    finally:    
        if request.method == "POST":
            try:
                name=request.form["depname"]
                locid=request.form["locid"]
                with sql.connect("Org.db") as con:
                    cur = con.cursor()
                    cur.execute("insert into departments (department_name,location_id) \
                            values (?,?)",(name,locid))
                    con.commit()
                msg="Department Added Successfully!"
                return render_template("add_department.html",msg=msg,data=rows)
            except:
                  print("Try agian")
        elif request.method=="GET":
            return render_template("add_department.html",data=rows)
        
        
#---------------------End Department Function---------


#---------------------Start List Department Function---
        
@app.route("/departmentslist")
def show_departments():
    try:
        with sql.connect("Org.db") as con:
            cur = con.cursor()
            cur.execute("select * from departments")
            rows = cur.fetchall()
            return render_template("departments_list.html",data=rows)
    except:
          print("Try agian")

#---------------------End List Department Function----
        
        
#---------------------Start Emp View Function---
        
@app.route("/viewemployees",methods=["POST","GET"])
def view_employees():
    if request.method == "POST":
        depid=request.form["info"]
        with sql.connect("Org.db") as con:
            cur = con.cursor()
            cur.execute("select * from employees where department_id = ?",(depid,))
            rows = cur.fetchall()
        return render_template("employees_list.html",data=rows)
    
    
#---------------------End Emp views Function---



#---------------------Start Update Department Function---


@app.route("/updateform",methods=["POST","GET"])
def updateform():
    if request.method == "POST":
        empid=request.form["id"]
        with sql.connect("Org.db") as con:
            cur = con.cursor()
            cur.execute("select * from jobs")
            rows = cur.fetchall()
            cur.execute("select * from departments")
            dep = cur.fetchall()
        return render_template("update_employee.html",data=empid,job=rows,dep=dep)
    
@app.route("/update",methods=["POST","GET"])
def update():
    if request.method == "POST":
        fname=request.form["fname"]
        lname=request.form["lname"]
        email=request.form["email"]
        phone=request.form["phone"]
        hire=request.form["hire"]
        jobid=request.form["jobid"]
        empid=request.form["id"]
        salary=request.form["salary"]
        depid=request.form["depid"]
        data=(fname,lname,email,phone,hire,jobid,salary,depid,empid)
        print(data)
        with sql.connect("Org.db") as con:
            cur = con.cursor()
            cur.execute("update employees set first_name = ?,last_name=?,email=?,phone_number=?,hire_date=?,job_id=?,salary=?,department_id=? where employee_id = ?",data)
            con.commit()
            msg="Employee Edited Successfully!"
        return render_template("home.html",msg=msg)
    
#---------------------End Update Department Function---
        



#---------------------Start Delete Function---

    

@app.route("/delete",methods=["POST","GET"])
def delete():
    delete_id=request.form["delEmp"]
    with sql.connect("Org.db") as con:
        cur = con.cursor()
        cur.execute("delete from employees where employee_id = ?",delete_id)
        con.commit()
        msg="Employee Deleted Successfully!"
    return render_template("home.html",msg=msg)

#---------------------End Delete Function---
    
if __name__ == "__main__":
    app.run()