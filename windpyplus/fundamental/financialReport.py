import pandas as pd 

from WindPy import w 
w.start()

from ..utils.tradedate import tradedate

def financial_report(stocks, rptdate='20170630'):
	data = w.wss(stocks, "sec_name,industry_sw,ev,val_pe_deducted_ttm,pb_lf,gr_ttm,deductedprofit_ttm,eps_ttm,ocfps_ttm,eps_exdiluted2,bps_new,stm_issuingdate,stm_predict_issuingdate",
		"industryType=1;unit=1;tradeDate=" + tradedate(0)[-1], "rptDate=" + rptdate,"currencyType=")
	df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
	df = df.dropna()
	df = df.sort_values(by='STM_ISSUINGDATE', ascending=False)
	print(len(df))
	return df

def financial_fastrep(stocks,rptdate='20170630'):
	pass