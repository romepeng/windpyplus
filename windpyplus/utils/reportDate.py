import pandas as pd 
from datetime import datetime, date, timedelta
import time, calendar
from windpyplus.utils.tradedate import tradedate
from WindPy import w
w.start()

class ReportUtils(object):
	REPORTQUARTER_MD = ['03-31','06-30','09-30','12-31']
	#PROFITNOTICE_DATE
	PROFITNOTICE_Q1_MD = ['01-23','04-30']
	PROFITNOTICE_Q2_MD = ['04-08','08-30']
	PROFITNOTICE_Q3_MD = ['07-15','10-31']
	PROFITNOTICE_Q4_MD = ['08-01','04-27']



	@classmethod			
	def reportDate(cls):
		now = datetime.now().date()
		print(now)
		print(now.year, now.month, now.day)
		reportdate = now
		return reportdate

	@classmethod
	def forecastReportDate(cls):



		pass




now = time.localtime()
print(now)
last_month = now[1] - 1 or 12
next_month = (now[1] + 3) % 12 or 12
print (last_month)
print (next_month)



if __name__ == '__main__':
	ReportUtils().reportDate()
	ReportUtils().forecastReportDate()
