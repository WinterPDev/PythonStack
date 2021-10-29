from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')
def dojo():
    return str('Dojo!')

@app.route('/say/<name>')
def flask(name):
    print(name)
    return str('Hello, ' + name)

@app.route('/repeat/<number>/<word>')
def repeat(number, word):
    return int(number) * word)

if __name__=="__main__": 
    app.run(debug=True)