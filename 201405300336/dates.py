#!/usr/bin/env python

def OneDay():
	from datetime import timedelta
	return timedelta(days = 1)

def Dates():
	from datetime import date
	dates = []
	startDate = date(2014, 3, 29)
	endDate = date.today()
	while startDate < endDate:
		dates.append(startDate)
		startDate += OneDay()
	return dates

def Yesterday(dates=Dates()):
	return dates[-1]

if __name__=="__main__":
	print OneDay()
	print Dates()
	print Yesterday()
	print Yesterday(Dates())
