from windpyplus.utils.tradedate import  tradedate, futuredate
import pandas as pd 
from WindPy import w 
w.start()

def companyScopeView():
	data = w.wset("companyscopegeneralview","enddate=" +tradedate(0)[1], "year=2016","sectorid=a001010100000000")
	df = pd.DataFrame(data=data.Data, index= data.Fields, columns=data.Codes).T
	print(df.head())
	return df 


def companyGenneralView():
	data = w.wset("listedcompanygenerayview","sectorid=a001010100000000")
	df = pd.DataFrame(data=data.Data, index= data.Fields, columns=data.Codes).T
	print(df.head())
	return df 


def securityGenneralView():
	data = w.wset("listedsecuritygeneralview","sectorid=a001010100000000")
	df = pd.DataFrame(data=data.Data, index= data.Fields, columns=data.Codes).T
	print(df.head())
	return df 

if __name__ == '__main__':
	companyScopeView()
	companyGenneralView()
	securityGenneralView()