from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    fruits = [
    {'fruit_image':'apple.png', 'fruit_name':'apple'},
    {'fruit_image':'blackberry.png', 'fruit_name':'blackberry'},
    {'fruit_image':'raspberry.png', 'fruit_name':'raspberry'},
    {'fruit_image':'strawberry.png', 'fruit_name':'strawberry'}
    ]

    return render_template("fruits.html", fruitslist=fruits)

if __name__=="__main__":   
    app.run(debug=True)    