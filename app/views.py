# external
import sys, os
from flask import render_template, redirect, request
from app import app

#internal
from form import EventForm
from events import add_event, get_events

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

	eventList = get_events()	

	return render_template("events.html",
					title = 'Events',
					eventList = eventList)

@app.route('/subscribe')
def subscribe():
	return render_template("subscribe.html", title = 'Subscribe')

@app.route('/contact')
def contact():
	return render_template("index.html", title = 'Contact')
