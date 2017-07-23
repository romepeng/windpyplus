import pandas as pd
from windpyplus.utils.tradedate import tradedate
from windpyplus.utils import remind as rm

from WindPy import *
w.start()
   
def valucationWind(stocklists):
    rm._write_msg('[Getting Data:]')
    df_V = pd.DataFrame()
    for code in stocklists:
        rm._write_inprogress()
        # sec_status,trade_code,
        data = w.wsd(code, "windcode,sec_name, close, ev,pe_ttm,val_pe_deducted_ttm,pe_lyr,pb_lf,pcf_ocflyr,west_eps_FY1,west_eps_FY2,estpe_FY1,estpe_FY2, estpeg_FTM,estpeg_FY1, industry_sw,concept",
                     tradedate(0)[0], tradedate(0)[1], "index=4;industryType=3")
        df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
        #df['ev'] = df['ev']/1.0E+8
        df_V = pd.concat([df_V, df])
        df_V = df_V.sort_values(by='INDUSTRY_SW')
    #df_V.to_excel("D:/Stock/tushare/stocklists.xlsx", sheet_name = tradedate(0)[-1])
    #rm._play_wav()
    print(len(df_V))
    return df_V

def PE_filter(stocklists, PE_ttm_max=100, PE_FY1_max = 50):
    df = valucationWind(stocklists)
    df = df[(df['VAL_PE_DEDUCTED_TTM']  < PE_ttm_max) & (df['ESTPE_FY1'] < PE_FY1_max)]
    print("PE_ttm < " + str(PE_ttm_max) + "and PE_FY1 < " + str(PE_FY1_max) +  " nums: {}".format(len(df)))
    return df.index.values

def PEG_filter(stocklists, PEG_max=1.5):
    df = valucationWind(stocklists)
    df = df[df['ESTPEG_FTM'] < PEG_max]
    print("PEG < " + str(PEG_max) + " nums: {}".format(len(df)))
    return df.index.values

def PB_filter(stocklists, PB_max=2):
    df = valucationWind(stocklists)
    df = df[(df['PB_LF']  < PB_max)]
    print("PB < " + str(PB_max) + " nums : {} ".format(len(df)))
    return df.index.values


