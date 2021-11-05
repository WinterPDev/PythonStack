from flask_app import app
from flask_app.controllers import approutes
# Always import Controllers into Server
if __name__ == "__main__":
    app.run(debug=True)