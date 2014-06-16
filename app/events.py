HOST = 'localhost'
USER = 'dungeonmaster'
PASSWD = 'yellow'
DB = 'events'

from app import app
#import MySQLdb

def add_event(title, timeDate, placeDesc, placeURL, description):

#	db =  MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
#
#	crosshairs = db.cursor()
#
#	query = "insert into events (title, timeDate, placeDesc, placeURL, description)"
#	query += " values ( '%s', '%s', '%s', '%s', '%s');" % (title, timeDate, placeDesc, placeURL, description)	
#
#	if app.debug == True:
#		print query
#
#	try:	
#		crosshairs.execute(query)
#		db.commit()
#	except:
#		db.rollback()

	return

def get_events():

	
#	db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
#
#	crosshairs = db.cursor()
#
#	query = "select * from events order by id desc limit 10;"
#
#	if app.debug == True:
#		print query
#
#	try:	
#		crosshairs.execute(query)
#		db.commit()
#	except:
#		db.rollback()
#
#	eventList = []
#	for row in crosshairs:
#		eventList.append({'title' : row[1],\
#					'timeDate' : row[2],\
#					'placeDesc' : row[3],\
#					'placeURL' : row[4],\
#					'description' : row[5] })
#
#	if app.debug == True:
#		for test in eventList:
#			print test
#
#	return eventList

	return
