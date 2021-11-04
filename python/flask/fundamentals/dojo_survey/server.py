from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keepitsecret"

@app.route("/")
def index():
    if "user" not in session:
        session["user"] = [{"name" : "",
        "location" : "",
        "language" : "",
        "comment" : ""}]

    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html",user=session["user"])


@app.route("/submit_info", methods=["POST"])
def vote():
    session["user"] = {
        "name":request.form["name"],
        "location":request.form["location"],
        "language":request.form["language"],
        "comment":request.form["comment"]
    }
    session.modified = True
    return redirect("/results")


@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)