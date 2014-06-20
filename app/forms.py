from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, BooleanField
from wtforms.validators import Required
class EventForm(Form):

	title = TextField('title', validators = [Required()])
	dateStart = TextField('dateStart',
					id='datepicker',
					validators = [Required()])
	timeStart = TextField('timeStart',
					id='datepicker',
					validators = [Required()])
	dateEnd = TextField('dateEnd',
					id='datepicker',
					validators = [Required()])
	timeEnd = TextField('timeEnd',
					id='datepicker',
					validators = [Required()])
	location = TextField('location',\
						validators = [Required()])
	mapsURL = TextField('mapsURL',\
						validators = [Required()])
	body = TextField('body',\
						validators = [Required()])

	
class LoginForm(Form):

	
	openid = TextField('openid', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)

