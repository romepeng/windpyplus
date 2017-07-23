import pandas as pd
from iwindpy_plus.utils.tradedate import tradedate
from WindPy import w
w.start()

def RS_OH(stocklists):
    data = w.wss(stocklists, 
        "sec_name,close,pct_chg,pct_chg_lowest_per,pct_chg_highest_per,pct_chg_5d,pct_chg_10d,pct_chg_1m,pct_chg_3m,pct_chg_6m,pct_chg_1y",
        "tradeDate= " +tradedate(0)[1] , "priceAdj=F;cycle=D;startDate=" + tradedate(365)[0],"endDate="+tradedate(365)[1])
    df = pd.DataFrame(data=data.Data, index= data.Fields, columns=data.Codes).T
    df = df.sort_values(by= 'PCT_CHG_1Y', ascending= False)
    #print(" stock num : {}".format(len(df)))
    return df

def newHighLow(stocklists):
    data = w.wss(stocklists, 
        "sec_name,close,history_high,history_low,stage_high,stage_low",
        "tradeDate= " +tradedate(0)[1] , "priceAdj=F;n=10;m=365")
    df = pd.DataFrame(data=data.Data, index= data.Fields, columns=data.Codes).T
    df = df.sort_values(by= 'HISTORY_HIGH', ascending= False)
    #print(" stock num : {}".format(len(df)))
    return df


def techIndictor(stocklists, days = 0):
    data = w.wss(stocklists, 
        "sec_name,close,ATR,BBI,BBIBOLL,BIAS,BOLL,CCI,DMA,DMI,EXPMA,MA,MACD,RC,ROC,RSI,SAR,STD,TRIX,vol_ratio",
        "tradeDate=" + tradedate(days)[0] ,
        "priceAdj=F;cycle=D;ATR_N=14;ATR_IO=1;BBI_N1=3;BBI_N2=6;BBI_N3=12;BBI_N4=24;BBIBOLL_N=10;BBIBOLL_Width=3;BBIBOLL_IO=1;BIAS_N=12;BOLL_N=26;BOLL_Width=2;BOLL_IO=1;CCI_N=14;DMA_S=10;DMA_L=50;DMA_N=10;DMA_IO=1;DMI_N=14;DMI_N1=6;DMI_IO=1;EXPMA_N=30;MA_N=3;MACD_L=26;MACD_S=12;MACD_N=9;MACD_IO=1;RC_N=50;ROC_interDay=12;ROC_N=6;ROC_IO=1;RSI_N=6;SAR_N=4;SAR_SP=2;SAR_MP=20;STD_N=26;TRIX_N1=12;TRIX_N2=20;TRIX_IO=1;VolumeRatio_N=50")
    df = pd.DataFrame(data=data.Data, index= data.Fields, columns=data.Codes).T
    df['CHG_5D/3D'] = 100*(df['MA'] - df['EXPMA'])/df['EXPMA']
    df = df.sort_values(by='CHG_5D/3D', ascending = False )
    return df

if __name__ == '__main__':
    from iwindpy_plus.stockPool.mystocks import stocklists
    df = newHighLow(stocklists)
    print(df)
    df = RS_OH(stocklists)
    print(df)

