from flask_app import app
from flask_app.controllers import users
# Always import Controllers into Server
if __name__ == "__main__":
    app.run(debug=True)