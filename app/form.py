from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required
class EventForm(Form):

	# create the fields for the form
	title = TextField('title', validators = [Required()])
	timeDate = TextField('timeDate',\
						validators = [Required()])
	placeDesc = TextField('placeDesc',\
						validators = [Required()])
	placeURL = TextField('placeURL',\
						validators = [Required()])
	description = TextField('description',\
						validators = [Required()])

	

