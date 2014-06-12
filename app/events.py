from app import app
from data import db_connect
import MySQLdb

def add_event(title, timeDate, placeDesc, placeURL, description):

	db = db_connect()
	cursor = db.cursor()

	query = "insert into events (title, timeDate, placeDesc, placeURL, description)"
	query += " values ( '%s', '%s', '%s', '%s', '%s');" % (title, timeDate, placeDesc, placeURL, description)	
	if app.debug == True:
		print query
	
	cursor.execute(query)
	db.commit()
	return		

	
	
