# external
import sys, os
from flask import flash, redirect, render_template, request, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import EventForm, LoginForm
from models import User
from events import add_event, get_events


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
	print '1'
	if resp.email is None or resp.email == "":
		print 
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
	print '2' 
	user = User.query.filter_by(email = resp.email).first()
	print '3' 
	if user is None:
		print 
		flash('Maybe you should listen to Gandalf.')
		return redirect(url_for('login'))
	print '4' 
	remember_me = False
	print '5' 
	if 'remember_me' in session:
		print 
		remember_me = session['remember_me']
		session.pop('remember_me', None)
	print '6' 
	login_user(user, remember = remember_me)
	print '7' 
	return redirect(url_for('admin'))

@app.route('/admin', methods = ['GET', 'POST'])
@login_required
def admin():

	return render_template('admin.html')

					
			
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
