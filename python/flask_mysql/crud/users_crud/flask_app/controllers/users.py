from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.user import User


@app.route("/")
def homeroute():
    return redirect("/users")

# ================================================
#   LIST USERS
# ================================================

@app.route("/users")
def index():
    all_users = User.pull_all_users()
    return render_template("users.html",all_users=all_users)

# ================================================
#   ADD USER
# ================================================

@app.route("/users/new")
def new_form():
    return render_template("new.html")

@app.route("/adduser", methods=["POST"])
def add_user():
    User.insert_user(request.form)
    return redirect("/users")

# ================================================
#   SHOW USER
# ================================================

@app.route("/users/<int:id>")
def show_user(id):
    data = {
        "id":id
    }
    user = User.get_user(data)
    return render_template("show.html", user=user)

# ================================================
#   EDIT USER
# ================================================

@app.route("/edit/<int:id>")
def edit_page(id):
    data = {
        "id":id
    }
    user = User.get_user(data)
    return render_template("edit.html", user=user)

@app.route("/edituser/<int:id>", methods=["POST"])
def edit_user(id):
    data = {
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    User.update_user(data)
    return redirect("/users")

# ================================================
#   DELETE USER
# ================================================

@app.route("/deleteuser/<int:id>")
def del_user(id):
    data = {
        "id":id
    }
    User.remove_user(data)
    return redirect("/users")