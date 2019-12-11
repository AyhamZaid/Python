# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:26:37 2019

@author: Ayham
"""
from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

DATABASE = "Stocks1.db"
app = Flask(__name__)

@app.route("/")
def index():
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
    res = cur.execute("select * from stokes")
    return render_template("index.html", stockes = res)

if __name__ == "__main__":
    app.run()