from windpyplus.utils.tradedate import  tradedate, futuredate
import pandas as pd 
from WindPy import w 
w.start()

def info(stocklists):
    data = w.wss(stocklists, "close,sec_name,industry_sw,ipo_date,mkt,sec_status,trade_code,compindex2,concept,marginornot,SHSC,SHSC2,sec_type,total_shares,float_a_shares,share_ntrd_prfshare,share_pledgeda,share_pledgeda_pct,share_rtd_unlockingdate,share_tradable_current,share_tradable_sharetype,holder_top10pct,holder_top10liqquantity,holder_controller,holder_name,","tradeDate=20170617;priceAdj=F;cycle=D;industryType=3;index=1;unit=1;order=0;rptDate=20161231")
    # holder_pctbyinst,holder_pctbyqfii,holder_pctbyinsur,holder_pctbyssfund, holder_price_fellowon,holder_price_mh,holder_price_Majorshareholders,holder_price_ESOP,holder_price_stockbasedcompensation
    #"roe_avg,roe_basic,roe_diluted,roe_deducted,roe_exbasic,roa2,roic,netprofitmargin,grossprofitmargin,deductedprofittoprofit,ocftocf,ocftosales,debttoassets,deducteddebttoassets,current,quick,cashtocurrentdebt,longdebttodebt,arturn,faturn,yoy_tr,yoy_or,yoyprofit,yoynetprofit,yoynetprofit_deducted,yoyocf,yoyroe,yoy_equity,tot_oper_rev,net_profit_is,tot_profit,np_belongto_parcomsh,net_cash_flows_oper_act","rptDate=20161231;unit=1;rptType=1")
    #print(data)
    df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
    #df.to_excel("D:/Stock/wind/info.xlsx", sheet_name = tradedate(0)[-1])
    #rm._play_wav()
    print(df.head())
    return df

def info1(stocklists):
    data = w.wss(stocklists, "close,sec_name,industry_sw,ipo_date,mkt,sec_status,trade_code,compindex2,concept,","tradeDate=20170617;priceAdj=F;cycle=D;industryType=3;index=1;unit=1;order=0;rptDate=20161231")
    #marginornot,SHSC,SHSC2,sec_type,total_shares,float_a_shares,share_ntrd_prfshare,share_pledgeda,share_pledgeda_pct,share_rtd_unlockingdate,share_tradable_current,share_tradable_sharetype,holder_top10pct,holder_top10liqquantity,holder_controller,holder_name,
    # holder_pctbyinst,holder_pctbyqfii,holder_pctbyinsur,holder_pctbyssfund, holder_price_fellowon,holder_price_mh,holder_price_Majorshareholders,holder_price_ESOP,holder_price_stockbasedcompensation
    #"roe_avg,roe_basic,roe_diluted,roe_deducted,roe_exbasic,roa2,roic,netprofitmargin,grossprofitmargin,deductedprofittoprofit,ocftocf,ocftosales,debttoassets,deducteddebttoassets,current,quick,cashtocurrentdebt,longdebttodebt,arturn,faturn,yoy_tr,yoy_or,yoyprofit,yoynetprofit,yoynetprofit_deducted,yoyocf,yoyroe,yoy_equity,tot_oper_rev,net_profit_is,tot_profit,np_belongto_parcomsh,net_cash_flows_oper_act","rptDate=20161231;unit=1;rptType=1")
    #print(data)
    df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
    #df.to_excel("D:/Stock/wind/info.xlsx", sheet_name = tradedate(0)[-1])
    #rm._play_wav()
    print(df.head())
    return df   

def dfToExcel(df, filename):
    df.to_excel("D:/Stock/wind/" + str(filename) + ".xlsx", sheet_name = tradedate(0)[-1])
    print(" df to_excel filename .")
    pass

def ROE_filter(stocklists, ROE_limit = 7.0):
    df = financialDataWind(stocklists)
    df = df[(df['ROA2'] > 7.0)  & (df['ROE_DEDUCTED'] > ROE_limit)]
    print("ROE and ROA2 > " + str(ROE_limit) + " Num:  {} ".format(len(df)))
    return df.index.values

