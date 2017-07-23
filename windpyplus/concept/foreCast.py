#from windpyplus.utils import WindPyStart
from windpyplus.utils.tradedate import tradedate
from windpyplus.stockPool.mystocks import stocklists
from windpyplus.stockPool.bigquantstocks import bqstocks
from windpyplus.utils.convertToWindCode import convertBQCode

def foreCastWind(stocklists):
	data = w.wss(stocklists, 
		"sec_name,profitnotice_style,profitnotice_change,profitnotice_lasteps,profitnotice_changemax,profitnotice_changemin,profitnotice_date,profitnotice_abstract,",
		"rptDate=20170630;unit=1")
	df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
	df = df[df['PROFITNOTICE_CHANGEMIN'] > -10]
	df = df.sort_values(by= 'PROFITNOTICE_DATE', ascending=False)
	print(df)
	return df

if __name__ == '__main__':
	stocklists = convertBQCode(bqstocks)
	df = foreCastWind(stocklists)
	from dfToExcel import dftoSameWorkbook, dfToExcel
	#from StockSector import MSCIAStock
	from StockSector import allAstock, MSCIAStock, allMainBoardStock
	mscistocks = MSCIAStock().index.values
	dfToExcel(df, "foreCastWind_bqstocks")
	#dfToExcel(foreCastWind(mscistocks), "foreCastWind_MSCIAStock")
