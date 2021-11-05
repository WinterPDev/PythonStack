from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.user import User


@app.route("/users")
def index():
    all_users = User.pull_all_users()
    return render_template("users.html",all_users=all_users)


@app.route("/users/new")
def new_form():
    return render_template("new.html")


@app.route("/adduser", methods=["POST"])
def add_user():
    User.insert_user(request.form)
    return redirect("/users")