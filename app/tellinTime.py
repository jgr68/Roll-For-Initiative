from datetime import datetime, timedelta
from pytz import timezone, utc

def make_datetime(date, time):
		
	local = timezone("America/New_York")
	naive =  datetime.strptime(date+" "+time.upper(), "%m/%d/%Y %I:%M%p")
	local_dt = local.localize(naive, is_dst=None)
	return local_dt.astimezone(utc)

def make_timestamp(dt):

	epoch = datetime(1970,1,1)
	td = dt - epoch
	return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e6
