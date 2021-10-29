from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keepitsecret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html")


@app.route("/vote", methods=["POST"])
def vote():
    session["name"] = request.form["name"]
    session["age"] = request.form["age"]
    session["movie"] = request.form["movie"]

    print("here is the form info:")
    print(request.form)
    print(request.form["name"])
    print(request.form["age"])
    print(request.form["movie"])
    return redirect("/results")

if __name__ == "__main__":
    app.run(debug=True)