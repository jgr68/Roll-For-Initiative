from app import app
from data import db_connect
import MySQLdb

def add_event(title, timeDate, placeDesc, placeURL, description):

	db = db_connect()
	crosshairs = db.cursor()

	query = "insert into events (title, timeDate, placeDesc, placeURL, description)"
	query += " values ( '%s', '%s', '%s', '%s', '%s');" % (title, timeDate, placeDesc, placeURL, description)	
	if app.debug == True:
		print query

	try:	
		crosshairs.execute(query)
		db.commit()
	except:
		db.rollback()

	db.close()
	return

def get_events():

	db = db_connect()
	crosshairs = db.cursor()

	query = "select * from events order by id desc limit 10;"

	if app.debug == True:
		print query

	try:	
		crosshairs.execute(query)
		db.commit()
	except:
		db.rollback()

	eventList = []
	for row in crosshairs:
		eventList.append({'title' : row[1],\
					'timeDate' : row[2],\
					'placeDesc' : row[3],\
					'placeURL' : row[4],\
					'description' : row[5] })

	if app.debug == True:
		for test in eventList:
			print test
	db.close()
	return eventList

