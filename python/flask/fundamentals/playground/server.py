from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/play")
@app.route("/play/")
@app.route("/play/<int:num>")
@app.route("/play/<int:num>/<string:inputcolor>")
def play_multi_colors(num=3, inputcolor='teal'):
    return render_template("play.html", num=num, inputcolor=inputcolor)

if __name__ == "__main__":
    app.run(debug=True)