# external
import sys, os
from flask import render_template, redirect, request
from app import app

#internal
from form import EventForm
from events import add_event

# ----------------------------------------------------------
@app.route('/')
@app.route('/index')
@app.route('/about')
def about():

	return render_template("index.html", title = 'About')


@app.route('/admin', methods = ['GET', 'POST'])
def admin():

	form = EventForm()
	if form.validate_on_submit():

		add_event(title = request.form['title'],\
				timeDate = request.form['timeDate'],\
				placeDesc = request.form['placeDesc'],\
				placeURL = request.form['placeURL'],\
				description = request.form['description'])

		return redirect('/events')
	return render_template('admin.html',\
						title = 'Admin',\
						form = form)
					
			
@app.route('/events')
def events():
	upcoming = [ # fake array of posts
		{
			'heading': "D&D Club : Monster Mash",
			'date_locale': "Friday - May 2nd @ BCC International Lounge",
			'body' :  "Come for free pizza and drinks as we celebrate the imminent\
				release of D&D Next! We're hosting an awesome Pathfinder\
				 tournament where players will lead parties of monsters \
				into combat! Make sure to check out the special ruleset for\
				the tournament by clicking\
				and to let us know if you have any questions."
					
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
			'heading': "Monthly meetup!",
			'date_locale': "5pm, first Friday of every month @ Busch Campus Center",
			'body' : 'Come by to see what we have to offer, find a group to play\
					with, and get a quick game in!'}
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
