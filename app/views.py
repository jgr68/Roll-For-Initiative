# external
import sys, os
from flask import flash, redirect, render_template, request, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import EventForm, LoginForm
from models import User, ROLE_USER, ROLE_ADMIN
from events import add_event, get_events

# ----------------------------------------------------------

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))



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
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
	user = User.query.filter_by(email = resp.email).first()
	if user is None:
		nickname = resp.nickname
		if nickname is None or nickname == "":
			nickname = resp.email.split('@')[0]
		user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
		db.session.add(user)
		db.session.commit()
	remember_me = False
	if 'remember_me' in session:
		remember_me = session['remember_me']
		session.pop('remember_me', None)
	login_user(user, remember = remember_me)
	return redirect(request.args.get('next') or url_for('index'))

@app.route('/admin', methods = ['GET', 'POST'])
def admin():

	form = EventForm()
	if form.validate_on_submit():

		add_event(title = request.form['title'],
				timeDate = request.form['timeDate'],
				placeDesc = request.form['placeDesc'],
				placeURL = request.form['placeURL'],
				description = request.form['description'])

		return redirect('/events')
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
