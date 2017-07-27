import pandas as pd 


from WindPy import w 
w.start()

def performance_express(stocks, rptdate='20170630'):
	data = w.wss(stocks, "sec_name, performanceexpress_perfexincome, performanceexpress_perfexnetfrofittoshareholder,performanceexpress_perfexepsdiluted,  performanceexpress_date", "unit=1; rptData="+rptdate)
	df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
	df = df.dropna()
	#df = df.sort_values(by= "PERFORMANCEEXPRESS_DATE", ascending=False)
	print(len(df))
	return df
