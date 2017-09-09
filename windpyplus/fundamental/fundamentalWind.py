from WindPy import w
w.start()
import pandas as pd
import subprocess

from ..utils.tradedate import tradedate
from ..utils import remind as rm

def financialDataWind(stocklists):
    field = ["sec_name,roe_avg,roe_basic,roe_diluted,roe_deducted,roe_exbasic,roa2,roic,netprofitmargin,grossprofitmargin,deductedprofittoprofit,ocftocf,ocftosales,debttoassets,deducteddebttoassets,current,quick,cashtocurrentdebt,longdebttodebt,arturn,faturn,yoy_tr,yoy_or,yoyprofit,yoynetprofit,yoynetprofit_deducted,yoyocf,yoyroe,yoy_equity,tot_oper_rev,net_profit_is,tot_profit,np_belongto_parcomsh,net_cash_flows_oper_act"]
    data = w.wss(stocklists, field, "rptDate=20161231;unit=1;rptType=1")
    df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
    print(df.head())
    return df

def dfToExcel(df, filename):
    df.to_excel("D:/Stock/tushare/" + str(filename) + ".xlsx", sheet_name = tradedate(0)[-1])
    print(" df to_excel filename .")
    pass

def ROE_filter(stocklists, ROE_limit = 7.0):
    df = financialDataWind(stocklists)
    #df = df[(df['ROA2'] > 7.0)  & (df['ROE_DEDUCTED'] > ROE_limit)]
    df = df[df['ROE_DEDUCTED'] > ROE_limit]
    print("ROE > " + str(ROE_limit) + " Num:  {} ".format(len(df)))
    return df.index.values

def netProfit_filter(stocklists, netProfit_limit = 1.0e+8):
    df = financialTTM(stocklists)
    df = df[df['DEDUCTEDPROFIT_TTM'] > netProfit_limit]
    print("DEDUCTEDPROFIT_TTM > " + str(netProfit_limit) + " Num:  {} ".format(len(df)))
    return df.index.values

def DB_filter(stocklists, DB_limit = 0.75):
    df = financialDataWind(stocklists)
    df = df[df['NP_BELONGTO_PARCOMSH'] < DB_limit]
    print("NP_BELONGTO_PARCOMSH > " + str(netProfit_limit) + " Num:  {} ".format(len(df)))
    return df.index.values

def cashFlow_filter(stocklists, cashFlow_percent = 0.95):
    df = financialTTM(stocklists)
    df = df[df['OCFPS_TTM'] > cashFlow_percent*df['EPS_TTM']]
    print("OCFPS_TTM'> " + str(cashFlow_percent) + "*EPS_TTM   Num:  {} ".format(len(df)))
    return df.index.values

def financialTTM(stocklists):
    data = w.wss(stocklists, "gr_ttm,or_ttm,profit_ttm,netprofit_ttm,deductedprofit_ttm,operatecashflow_ttm,cashflow_ttm,eps_ttm,ocfps_ttm,orps_ttm,cfps_ttm","unit=1; tradeDate=" + str(tradedate(0)[1]) + ";year=2016")
    df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
    return df

def growth(stocklists, reportDate= "20161231"):
    data = w.wss(stocklists, "yoyeps_basic,yoyeps_diluted,yoyocfps,yoy_tr,yoy_or,yoyop,yoyop2,yoyebt,yoyprofit,yoynetprofit,yoynetprofit_deducted,yoyocf,yoyroe,yoy_cash,yoy_equity,yoycf,yoydebt,yoy_assets","rptDate=" + str(reportDate) +";rptType=1")
    df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
    return df
    
def growth_filter(stocklists, growth_min = 6):
    df_1Y = growth(stocklists, "20161231")
    df_1Y = df_1Y[df_1Y['YOYNETPROFIT_DEDUCTED'] > growth_min]
    df_2Y = growth(stocklists, "20151231")
    df_2Y = df_2Y[df_2Y['YOYNETPROFIT_DEDUCTED'] > 0]
    df_N = growth(stocklists, "20170331")
    df_N = df_N[df_N['YOYNETPROFIT_DEDUCTED'] > 2*growth_min]
    stocks = [s for s in df_2Y.index if s in df_1Y.index]
    stocks = [s for s in df_N.index if s in stocks]
    print("YOYNETPROFIT_DEDUCTED'> " + str(growth_min) + " Num:  {} ".format(len(stocks)))
    return stocks

def multi_filter(stocklists,ROE_limit=8, growth_min=15, netProfit_limit=1.0e+8):
    roe_list = ROE_filter(stocklists, 8) 
    #cashflow_list = cashFlow_filter(stocklists)
    growth_list = growth_filter(stocklists, 15)
    netProfit_list = netProfit_filter(stocklists)
    #result_list = [s for s in roe_list if s in cashflow_list]
    result_list = [ s for s in roe_list if s in growth_list]
    result_list = [s for s in result_list if s in netProfit_list]
    print("ROE>8, growth>15, netProfit>1.0e+8" + "Num: {} ".format(len(result_list)))
    return result_list

if __name__ == '__main__':
    from windpyplus.stockPool.mystocks import stocklists
    print(stocklists)
    from windpyplus.stockSector.StockSector import HKToChina
    stocklists = HKToChina()
    len(financialDataWind(stocklists))
    print(ROE_filter(stocklists, 8))
    #print(netProfit_filter(stocklists, 1.5e+8))
    #print(financialTTM(stocklists))
    print(cashFlow_filter(stocklists))
    print(growth_filter(stocklists, 5))
    print(multi_filter(stocklists))

