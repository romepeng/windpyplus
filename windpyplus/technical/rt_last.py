from iwindpy_plus.utils.dfToExcel import dfToExcel
import pandas as pd 
from WindPy import w 
w.start()


def rtLast(stocklists):
	data = w.wsq(stocklists, "rt_last,rt_pct_chg,rt_activenetin_amt,rt_activeinvol_prop,rt_mf_ratio,rt_mf_ratio_5d,rt_mf_ratio_10d,rt_mf_ratio_20d,rt_mf_ratio_60d,rt_mf_days_5d,rt_mf_days_10d,rt_mf_days_20d,rt_mf_days_60d")
	df = pd.DataFrame(data=data.Data, index= data.Fields, columns=data.Codes).T
	df = df.sort_values(by= 'RT_MF_RATIO_10D', ascending= False)
	print(" real last price stock num : {}".format(len(df)))
	return df

if __name__ == '__main__':
	from iwindpy_plus.stockPool.mystocks import stocklists
	df = rtLast(stocklists)
	dfToExcel(df, 'mystocks_realTrade_stat')

