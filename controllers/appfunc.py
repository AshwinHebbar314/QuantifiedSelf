from flask_login import login_user, logout_user, current_user, login_required
from flask import current_app as app, render_template, request, redirect, flash
from application.models import *
from datetime import datetime
import matplotlib.pyplot as plt 
import numpy as np

@app.route("/")
def landing():
    return render_template("index.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("signin.html")
    elif request.method == "POST":
        user = request.form["user_name"]
        passw = request.form["passw"]
        loginu = User.query.filter_by(name=user).first()
        if(passw == loginu.password):
            try:
                login_user(loginu)
            except:
                return f"User {user} does not exist, you can <a href = '/signup'> Create a new user by clicking here</a>"
            return redirect("/dashboard")
        else:
            return f"Wrong Password, please <a href = '/login'> try again </a>"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

