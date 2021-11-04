from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!' 

@app.errorhandler(404)
def page_not_found(e):
    return str('Sorry No Response. Try Again.')

@app.route('/dojo')
def dojo():
    return str('Dojo!')

@app.route('/say/<string:name>')
def flask(name):
    print(name)
    return str('Hello, ' + name)

@app.route('/repeat/<int:number>/<string:word>')
def repeat(number, word):
    words = ''

    for i in range(0, number):
        words += f"<p>{word}<p>"
    return words

if __name__=="__main__": 
    app.run(debug=True)