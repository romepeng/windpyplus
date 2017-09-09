from windpyplus.stockPool.mystocks import stocklists
from windpyplus.stockSector.StockSector import allAstock, HKToChina, allMainBoardStock
from windpyplus.fundamental.fundamentalWind import  financialDataWind, netProfit_filter, ROE_filter, growth_filter, cashFlow_filter, multi_filter
from windpyplus.utils.dfToExcel import dfToExcel


print(stocklists)
#print(ROE_filter(stocklists, 8))
#print(netProfit_filter(stocklists, 1.5e+8))
#print(growth_filter(stocklists, 5))
print(multi_filter(stocklists))

stock_hktochina = list(HKToChina().index.values)

df_mylist = financialDataWind(stocklists)
dfToExcel(df_mylist, 'mystock_finacial')
dfToExcel(financialDataWind(multi_filter(list(allAstock().index))), 'allstock_filter')

