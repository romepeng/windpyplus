# -*- coding: utf-8 -*-

"""Main module."""
#import sys
#sys.path.append(" D:\\windpyplus")

#import site; site.getsitepackages()
import pandas as pd

import windpyplus

#from windpyplus.stockSector.StockSector import allAstock, MSCIAStock
from windpyplus.fundamental.foreCastWind import foreCastWind
from windpyplus.utils.convertToWindCode import convertBQCode, convertCode
from windpyplus.utils.dfToExcel import dftoSameWorkbook, dfToExcel
from windpyplus.fundamental.valucation import valucationWind

allastocks = list(allAstock().index.values)


def fiter_ForecastValucation(qt = '20170630', CHG_MIN= 7):
    allastocks = list(allAstock().index.values)
    df = foreCastWind(allastocks, qt)
    df = df[df['PROFITNOTICE_CHANGEMEAN'] > CHG_MIN]
    print(df.head())
    
    stocklists = df.index.values
    df_V = valucationWind(stocklists)
    print(df_V.head())
    df_f = pd.merge(df_V,df, how='left')
    
    dfToExcel(df_f, "filter_valucation_forecast_"+ str(qt)+"_"+ str(CHG_MIN)) 
    print('num of filter_forecastValucation : {}'.format(df_f)) 
    return df_f

if __name__ == '__main__':

    df =fiter_ForecastValucation(CHG_MIN= 10)
    print(df)

    print(tradedate(0))
