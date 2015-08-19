from datetime import datetime, timedelta

def iterate(fromDate, toDate, inFormat="%Y%m%d", outFormat="%Y%m%d"):
	"""
	* Generate date range starting from date(in YYYYMMDD) format 
	to date (in YYYYMMDD) 
	* Start and endate are included in the output.  
	"""
	_st = datetime.strptime(fromDate, inFormat)
	_et = datetime.strptime(toDate, outFormat)
	_delta = (_et - _st).days + 1

	for i in range(_delta):
		yield (_st + timedelta(days=i)).strftime(outFormat)


def add(fromDate, delta, inFormat="%Y%m%d", outFormat="%Y%m%d"):
	"""
	Add/Subtract number of days to a given date. 
	"""
	given = datetime.strptime(fromDate, inFormat)
	return (given + timedelta(days=delta)).strftime("%Y%m%d")

def subtract(fromDate, delta, **kwargs):
	return add(fromDate, -1 * delta, **kwargs)
	