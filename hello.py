from flask import Flask, render_template



# create a Flask instance
app= Flask(__name__)

# safe
# capitalizze
# lower 
# upper
# title
# trim
# striptags

#  create a route decorator

@app.route('/')

# def index():
	# return "<h1>Hello World!</h2>"
def index():
	first_name="Suryansh"
	stuff="This is <strong>Bold</strong> Text"
	# stuff2="this is <strong>Bold</strong> Text"
	favourite_pizza=["pepperoni","macroni","cheese",41]

	return render_template("index.html",stuff=stuff,
		first_name=first_name,favourite_pizza=favourite_pizza)

# localhost:5000/user/suryansh
@app.route('/user/<name>')
# def user(name):
# 	return "<h1>Hello {} World!</h2>".format(name)
def user(name):
	return render_template("user.html", user_name=name)

# custom error pages

# invalid url
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404
# internal Serveer error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"),500
	
