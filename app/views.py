import sys, os
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/about')
def about():

	return render_template("index.html", title = 'About')

@app.route('/events')
def events():
	upcoming = [ # fake array of posts
		{
			'heading': "Awesome New Event!",
			'date_locale': "Monday - January 1st @ The Cove (BCC)",
			'body' :  'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
                                  Vivamus a magna ut est mattis mollis et in est. Praesent\
                                  aliquam blandit lectus non blandit.'
		},
		{
			'heading': "Come join us!",
			'date_locale': "Friday - August 9th @ Werblin (Busch Campus)",
			'body' : 'Vivamus faucibus bibendum mi, non pretium est ultrices et.\
                                   Donec risus mauris, laoreet eget pretium sed, cursus sed\
                                   nunc. Morbi porta lacus ut condimentum ultricies. Nam\
                                   ligula lorem, tempor et elit id, ullamcorper vestibulum mauris.'
		}
	]
	weekly = [ # fake array of posts
		{
			'heading': "Weekly meetup!",
			'date_locale': "Fridays 1pm-3pm @ Rutgers Student Center",
			'body' : 'Integer eget libero vitae risus consequat consectetur.\
                                   Nam vestibulum nunc vitae neque scelerisque porttitor.\
                                   Cras ornare lectus enim, ut placerat justo ultricies sed.'
		},
		{
			'heading': "Business as usual!",
			'date_locale': "Saturdays 10am-12pm @ LSC (Livingston)",
			'body' : 'Mortiam imperdiet nibh felis, quis malesuada dui faucibus ac.\
                                   Nunc elit magna, iaculis id mi suscipit, dignissim interdum elit.\
                                   Aliquam erat volutpat. Maecenas dui nibh, vestibulum ut nulla at,\
                                    aliquet tempus purus. Maecenas consequat purus vitae eleifend sollicitudin.'
		}
	]

	return render_template("events.html",
					title = 'Events',
					weekly = weekly,
					upcoming = upcoming)

@app.route('/subscribe')
def subscribe():
	return render_template("subscribe.html", title = 'Subscribe')

@app.route('/contact')
def contact():
	return render_template("index.html", title = 'Contact')

