# external
import sys, os
from flask import flash, redirect, render_template, request, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import EventForm, LoginForm
from models import User, ROLE_ADMIN
from events import add_event, get_events
from tellinTime import make_datetime, make_timestamp

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/')
@app.route('/index')
@app.route('/about')
def about():
	return render_template("index.html", title = 'About')

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():

	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('admin'))
		
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
	return render_template('login.html',
						title = 'Sign In',
						form = form,
						providers = app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
	if resp.email is None or resp.email == "":
		print 
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
	user = User.query.filter_by(email = resp.email).first()
	if user is None:
		#user = User(email=resp.email, role=ROLE_ADMIN)
		#db.session.add(user)
		#db.session.commit()
		flash('Maybe you should listen to Gandalf.')
		return redirect(url_for('login'))
	remember_me = False
	if 'remember_me' in session:
		print 
		remember_me = session['remember_me']
		session.pop('remember_me', None)
	login_user(user, remember = remember_me)
	return redirect(url_for('admin'))

@app.route('/admin', methods = ['GET', 'POST'])
@login_required
def admin():

	form = EventForm()
	if request.method == 'POST':
		title = form.title.data
		start_datetime = make_datetime(date=form.dateStart.data,
									time=form.timeStart.data)
		end_datetime = make_datetime(date=form.dateEnd.data,
									time=form.timeEnd.data)
		location = form.location.data
		mapsURL = form.mapsURL.data
		body = form.body.data

		print 'title: ',title
		print 'start_datetimei: ',start_datetime
		print 'start_unix: ',make_timestamp(start_datetime)
		print 'end_datetime: ',end_datetime	
		print 'end_unix: ',make_timestamp(end_datetime)
		print 'location: ',location
		print 'mapsURL: ',mapsURL
		print 'body: ',body

	return render_template('admin.html',
						title = 'Admin',
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
 
@app.route('/logout')
@login_required
def logout():
	
	logout_user()
	return redirect(url_for('login'))
