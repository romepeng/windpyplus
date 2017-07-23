import pandas as pd
from windpyplus.utils.tradedate import tradedate
from WindPy import w
w.start()

def Concept(stocklists):
    data = w.wss(stocklists,"sec_name,concept","tradeDate="+ tradedate(0)[1] )
    df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
    return df

def Industry(stocklists):
    data = w.wss(stocklists,"sec_name,industry_gics,industry_citic,industry_sw","industryType=1;tradeDate="+ tradedate(0)[1] )
    df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
    return df

if __name__ == '__main__':
	from windpyplus.stockPool.mystocks import stocklists
	print(Concept(stocklists))
	print(Industry(stocklists))


