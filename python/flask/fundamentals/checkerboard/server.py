from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/<int:row>")
@app.route("/<int:row>/<int:column>")
@app.route("/<int:row>/<int:column>/<string:inputcolor>/<string:inputcolor2>")
def play_multi_colors(row=4, column=4, inputcolor='black', inputcolor2='darkred'):
    return render_template("index.html", row=row, column=column, inputcolor=inputcolor, inputcolor2=inputcolor2)


if __name__ == "__main__":
    app.run(debug=True)