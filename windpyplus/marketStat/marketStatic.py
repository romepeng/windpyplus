from windpyplus.utils.tradedate import  tradedate, futuredate
import pandas as pd 
from WindPy import w 
w.start()

def marketSiceSatic():
	data = w.wset("stockmarketsizestatistics","market=shsz")
	df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
	print(df.head())
	return df


def marketScaleStat():
	data = w.wset("marketscalestatisticbywind","reporttype=y1;startdate=" +tradedate(90)[0], "enddate="+tradedate(0)[1])
	df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
	print(df.head())
	return df

def indScaleStat():
	data = w.wset("indscalestatbywind","industrytype=证监会行业;enddate=" +tradedate(0)[1])
	df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
	print(df.head())
	return df

def mkTradeStat():
	data = w.wset("mkttradestatsec","startdate="+tradedate(365)[0] ,"enddate="+tradedate(0)[1],"sectorid=a001010100000000")
	df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
	df = df.sort_values(by='date', ascending = False)
	print(df.head())
	return df


if __name__ == '__main__':
	mkTradeStat()