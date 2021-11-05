from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.friend import Friend

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)
    # relevant code snippet from server.py

@app.route('/create_friend', methods=["POST"])
def create_friend():
    data = {
    "fname": request.form["fname"],
    "lname" : request.form["lname"],
    "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')
