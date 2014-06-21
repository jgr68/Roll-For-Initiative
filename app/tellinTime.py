from datetime import datetime, timedelta
from pytz import timezone, utc

LOCALE = "America/New_York"

def make_datetime(date, time):
		
	local = timezone(LOCALE)
	naive =  datetime.strptime(date+" "+time.upper(), "%m/%d/%Y %I:%M%p")
	local_dt = local.localize(naive, is_dst=None)
	return local_dt.astimezone(utc)

def make_timestamp(dt):

	local = timezone(LOCALE)
	local_epoch = local.localize(datetime(1970,1,1), is_dst=None)
	epoch = local_epoch.astimezone(utc)
	td = dt - epoch
	return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e6

def unix2human(timestamp):

	value = datetime.fromtimestamp(timestamp)
	return value.strftime('%b %d %Y - %H:%M%P')
