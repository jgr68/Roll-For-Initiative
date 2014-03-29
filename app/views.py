from flask import render_template
from app import app

@app.route('/')
@app.route('/about')
def about():

	return render_template("index.html",
					title = 'About',
					heading = 'About Roll for Initiative')

@app.route('/events')
def events():
	upcoming = [ # fake array of posts
		{
			'heading': "We're going to have a meeting about meetings!",
			'date_locale': "Monday, January 1st",
			'body' : 'Well we see now that we are doing something very\
						interesting with our eyes and looking for a \
						spotted toad lodged firmly in cubical space \
						with lemon pi. Yes we are.'
		},
		{
			'heading': "We're going frolic in a field!",
			'date_locale': "Tuesday, April 32nd",
			'body' : 'Well we see now that we are doing something very\
						interesting with our eyes and looking for a \
						spotted toad lodged firmly in cubical space \
						with lemon pi. Yes we are.'
		}
	]
	weekly = [ # fake array of posts
		{
			'heading': "We're going to have a meeting about meetings!",
			'date_locale': "Monday, January 1st",
			'body' : 'Well we see now that we are doing something very\
						interesting with our eyes and looking for a \
						spotted toad lodged firmly in cubical space \
						with lemon pi. Yes we are.'
		},
		{
			'heading': "We're going frolic in a field!",
			'date_locale': "Tuesday, April 32nd",
			'body' : 'Well we see now that we are doing something very\
						interesting with our eyes and looking for a \
						spotted toad lodged firmly in cubical space \
						with lemon pi. Yes we are.'
		}
	]

	return render_template("events.html",
					title = 'Events',
					heading = 'We socialize',
					weekly = weekly,
					upcoming = upcoming)

@app.route('/subscribe')
def subscribe():
	return render_template("index.html",
					title = 'Subscribe',
					heading = 'We haz a mailing list')

@app.route('/contact')
def contact():
	return render_template("index.html",
					title = 'Contact',
					heading = 'Contact us right nao')

