from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), index = True, unique = True)
	role = db.Column(db.SmallInteger, default = ROLE_USER)

	# should return true if we want user to be allowed to authenticate
	def is_authenticated(self):
		return True

	# return true unless user has been banned
	def is_active(self):
		return True

	# should return true only for fake users that are not supposed to log in
	def is_anonymous(self):
		return False

	# should return a unique identifier for the user in unicode format
	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.email)

class Event(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(300))
	eventTimedate = db.Column(db.DateTime)
	postTimestamp = db.Column(db.DateTime)
	locationDesc = db.Column(db.String(200))
	locationURL = db.Column(db.String(100))

	def __repr__(self):

		return '<Event %r>' % (self.title)
