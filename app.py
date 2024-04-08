from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

products = {
   1:{
        "description": "Jeans",
        "price": 10.99,
        "amount": 5,
        "image_url": "https://d11ak7fd9ypfb7.cloudfront.net/styles1100px/MV25YNR.jpg"
    },
    2:{
        "description": "Stylish Jeans",
        "price": 19.99,
        "amount": 10,
        "image_url": "https://d11ak7fd9ypfb7.cloudfront.net/styles1100px/MV26YNR.jpg"
    },
    3:{
        "description": "Dress",
        "price": 15.50,
        "amount": 3,
        "image_url": "https://d11ak7fd9ypfb7.cloudfront.net/styles1100px/FC57BKR.jpg"
    },
    4:{
        "description": "Dress 2",
        "price": 19.99,
        "amount": 10,
        "image_url": "https://d11ak7fd9ypfb7.cloudfront.net/styles1100px/2003BKR.jpg"
    },
    5:{
        "description": "Dress 3",
        "price": 19.99,
        "amount": 10,
        "image_url": "https://d11ak7fd9ypfb7.cloudfront.net/styles1100px/2003BKR.jpg"
    },
    6:{
        "description": "Dress 4",
        "price": 19.99,
        "amount": 10,
        "image_url": "https://d11ak7fd9ypfb7.cloudfront.net/styles1100px/2003BKR.jpg"
    }
    
}

def validate_username(username):
    # Username should be alphanumeric and at least 4 characters long
    return re.match(r'^[a-zA-Z0-9]{4,}$', username) is not None

def validate_password(password):
    # Password should be at least 6 characters long
    return len(password) >= 6

def validate_email(email):
    # Email validation using a simple regex
    return re.match(r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+$', email) is not None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home/",  methods=["GET"]) 
def home():
    return render_template("home.html")

@app.route("/contacts/",  methods=["GET"]) 
def contacts():
    return render_template("contacts.html")


@app.route('/register/', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    
    errors = {}

    if not validate_username(username):
        errors['username'] = 'Username must be alphanumeric and at least 4 characters long.'

    if not validate_password(password):
        errors['password'] = 'Password must be at least 6 characters long.'

    if not validate_email(email):
        errors['email'] = 'Invalid email address.'

    if errors:
        return render_template('index.html', errors=errors)
    else:
        # Here you would typically save the user to a database
        # For simplicity, we'll just print the user information
        print(f'New User Registered:\nUsername: {username}\nPassword: {password}\nEmail: {email}')
        return render_template("home.html")

@app.route("/add-product/",  methods=["GET"]) 
def add_item_form():
    return render_template("forms.html")

    
@app.route("/add-product/",  methods=["POST"]) 
def add_item_data():
     form_input = request.form.get("name") 
     product = {"description": form_input}
     #form_input = request.form.get("price") 
     #product = {"price": form_input}
     index = len(products)+1
     products[index]= product        #add product
     return redirect(url_for("shop"))
     


@app.route("/order/<int:id>",  methods=["POST"])  
def order(id):
    print( request )
    product = products[id]
    if product["amount"] > 0:
        product["amount"] -= 1
        return product
    else:
        return "<h2>Out of Stock</h2>"

@app.route("/shop/")
@app.route("/shop/<search_term>")
def shop(search_term=""):
    search_results=[]
    for product in products.values():
        if search_term in product["description"]:
            search_results.append(product)

    return render_template("shop.html", products=search_results)


if __name__ == '__main__':
    app.run(debug=True, port=8080)