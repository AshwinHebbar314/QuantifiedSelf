from flask_login import login_user, logout_user, current_user, login_required
from flask import current_app as app, render_template, request, redirect, flash
from application.models import *
from datetime import datetime
import matplotlib.pyplot as plt 
import numpy as np
from controllers.miscmethods import *

@app.route("/dashboard/create_tracker", methods=["GET", "POST"])
@login_required
def create_tracker():
    if request.method == "GET":
        return render_template("create_tracker.html")
    elif request.method == "POST":
        name = request.form["tname"]
        details = request.form["tdet"]
        type = request.form["ttype"]
        choices = request.form["mulcho"]
        choices = str(choices.split(' '))
        print(choices)

        upd = Tracker(userid=current_user.id, name=name,  type=type, choices=choices,
                      details=details, time=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        db.session.add(upd)
        db.session.commit()
        return redirect("/dashboard")


@app.route("/dashboard/<tid>/details", methods=["GET"])
@login_required
def tracker_details(tid):
    create_plot(tid)
    tracker = Tracker.query.filter_by(id=tid).first()
    logs = Logs.query.filter_by(tid=tid, userid=current_user.id).all()
    return render_template("tracker_details.html", tracker=tracker, logs=logs)




@app.route("/dashboard/<tid>/delete", methods=["GET"])
@login_required
def delete_tracker(tid):
    logs = Logs.query.filter_by(tid=tid).delete()
    db.session.commit()
    tracker = Tracker.query.filter_by(id=tid).delete()
    db.session.commit()
    return redirect("/dashboard")