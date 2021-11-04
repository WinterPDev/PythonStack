from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keepitsecret"

@app.route("/", methods=['POST', 'GET'])
def counter():
    if 'ticker' not in session:
        session["ticker"] = 1
    if request.method == 'POST':
        session["ticker"] += 2
    return render_template('index.html',ticker=session["ticker"])

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
