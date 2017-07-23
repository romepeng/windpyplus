from windpyplus.utils.tradedate import  tradedate, futuredate
import pandas as pd 
from WindPy import w 
w.start()

def limitToFree():
	data = w.wset("limitingtofreeofcompanydetail","startdate="+ futuredate(180*4)[0],"enddate=" + futuredate(180*4)[1],"sectorid=a001010100000000;search=")
	df = pd.DataFrame(data=data.Data, index= data.Fields, columns=data.Codes).T
	#print(df.head())
	return df 
	
def blockTradeRecord():
	data = w.wset("blocktraderecord","startdate=" +tradedate(20)[0] , "enddate="+tradedate(20)[1],"sectorid=a001010100000000")
	df = pd.DataFrame(data=data.Data, index= data.Fields, columns=data.Codes).T
	df = df.sort_values(by='trade_date', ascending=False)
	#print(df.head(30))
	return df 

if __name__ == '__main__':
	from windpyplus.utils.dfToExcel import dfToExcel
	dfToExcel(limitToFree(), '限售股解禁_2Y' )
	dfToExcel(blockTradeRecord(), '大宗交易')
