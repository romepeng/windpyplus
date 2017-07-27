# test scripts in project


import pandas as pd 


from WindPy import w 
w.start()

from windpyplus.utils.tradedate import tradedate
from windpyplus.fundamental.performanceExpress import performance_express
from windpyplus.fundamental.financialReport import financial_report
from windpyplus.stockSector.StockSector import allAstock

allstocks = list(allAstock().index.values)
print(tradedate())
#print(performance_express(list(allAstock().index.values)))
print(financial_report(allstocks))