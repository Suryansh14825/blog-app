from flask import Flask,render_template


# create a flask instance
app=Flask(__name__)
# upar wala saari file kkhoj leta directory mein
# creaate a route decorator
@app.route('/')
# def index():
#     return "<h1> Hello World!</h1>"
# below are some filter for jinja 
# safe- it makes bold and include html tags 
# capitalize
# lower
# upper
# title
# trim remove spaces 
# striptags udaa dega html ttags
def index():
    first_name="John"
    stuff="This is bold text"
    favourite_pizza=["pepperoni","mushroom","pizza","chilli",41]
    return render_template("index.html", first_name=first_name,
        stuff=stuff,favourite_pizza=favourite_pizza)

#localhost:5000/user/Suryansh
@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name=name)
# create custom error pages

# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500


# if __name__ == "__main__":
# 	app.run(host="localhost", port=int("5500")) 