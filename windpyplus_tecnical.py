# -*- coding: utf-8 -*-

import pandas as pd

from windpyplus.utils.tradedate import tradedate
from windpyplus.stockSector.StockSector import allAstock, MSCIAStock
from windpyplus.fundamental.foreCastWind import foreCastWind
from windpyplus.utils.convertToWindCode import convertBQCode, convertCode
from windpyplus.utils.dfToExcel import dftoSameWorkbook, dfToExcel
from windpyplus.fundamental.valucation import valucationWind
from windpyplus.stockPool import mystocks
from windpyplus.technical.technicalAnalysis import MA_Periods, Return_Periods

allastocks = list(allAstock().index.values)

def tecnical_filter(stocks):
    df_MA = MA_Periods(stocks)
    df_R = Return_Periods(stocks)
    print(df_MA)
    print(df_R)
    #return df


if __name__ == '__main__':

    tecnical_filter(mystocks.stocklists)
