import MySQLdb

# login details
#HOST = 'localhost'
#SEC_USER = 'sec_user'
#SEC_PASSWD = '4Fa98xkHVd2XmnfK'
#DB = 'secure_login'

# switch over to mongno and use mysql for logins
HOST = 'localhost'
USER = 'root'
PASSWD = 'yellow'
DB = 'events'

CAN_REGISTER = 'any'
DEFAULT_ROLE = 'member'

SECURE = False # dev mode

def db_connect():

	# connect to the msyql database
	db = MySQLdb.connect(host = HOST,\
						user = USER,
						passwd = PASSWD,
						db = DB)
	return db

					
