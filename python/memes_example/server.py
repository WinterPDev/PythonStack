from flask_app import app
from flask_app.controllers import memes

# Always import Controllers into Server

if __name__ == "__main__":
    app.run(debug=True)


