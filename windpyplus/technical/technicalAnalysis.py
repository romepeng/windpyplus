#from pandas import DataFrame, Series
import pandas as pd
from  WindPy import *
import datetime
w.start()
from ..utils.tradedate import tradedate

class PriceAnalysis(object):
    """ Stock Price Analysis"""
    def __init__(self, code, period):
        self.code = code
        self.period = period  # period = days of calender

    def Price(self):
        field = ["close"]
        data = w.wsd(self.code, field, "ED0D", tradedate(self.period)[1])
        df = pd.DataFrame(data.Data, index=data.Times, columns=data.Codes)
        df.index = ["price"]
        return df

    def SecName(self):
        field = ["sec_name"]
        data = w.wss(self.code, field)
        df = pd.DataFrame(data.Data, index=data.Fields, columns=data.Codes)
        df.index = ["SNAME"]
        return df
       
    def PriceSeries(self):
        field = ["close"]
        data = w.wsd(self.code, field, tradedate(self.period)[0], tradedate(self.period)[1], "Fill=Previous;PriceAdj=F")
        df = pd.DataFrame(data.Data,index=data.Codes,columns=data.Times).T
        return df

    def Return(self): 
        df = PriceAnalysis(self.code, self.period).PriceSeries()
        df = (df/df.shift(1) - 1)
        df_R = df.sum()*100
        return df_R


    def MA(self):
        df = PriceAnalysis(self.code, self.period).PriceSeries()
        ma = df.mean()
        return ma

    def OH(self):  # ???
        df = PriceAnalysis(self.code, self.period).PriceSeries()
        df_max = df.max()
        #print(df.max)
        #oh =  (close/max -1)*100.
        return df_max


def MA_Periods(code, periods_list=[7, 15, 30, 90, 182, 365, 2*365, 3*365]):
    df = PriceAnalysis(code,period= 20).Price()
    #print(type(df))
    #df  = pd.DataFrame()
    for days in  periods_list:
        PA = PriceAnalysis(code, days)
        MA = PA.MA()
        index = "MA" + str(days)
        d = {index: pd.Series(MA.values, MA.index)}
        df1 = pd.DataFrame(d).T
        df = pd.concat([df, df1])
    #print(df)
    return(df)
  

def Return_Periods(code, periods_list=[7, 15, 30, 90, 182, 365, 2*365, 3*365]):
    df = PriceAnalysis(code,period= 20).SecName()
    #print(type(df))
    for days in  periods_list:
        PA = PriceAnalysis(code, days)
        chg = PA.Return()
        index = "Chg_" + str(days)
        d = {index: pd.Series(chg.values, chg.index)}
        df1 = pd.DataFrame(d).T
        df = pd.concat([df, df1])
    #print(df)
    return df
   

def OH_Periods(code, periods_list=[182, 365, 3*365, 5*365, 10*365]):

    for days in  periods_list:
        PA = PriceAnalysis(code, days)
        OH = PA.OH()
        print(days)
        print(OH)

if __name__ == '__main__':
    print(starttradedate(30),lasttradedate())
    code = ["002139.SZ, 002460.SZ, 600373.SH, 002422.SZ, 600516.SH, 002230.SZ, 601318.SH, 600519.SH"]
    PF = PriceAnalysis(code, period=30)
    df = PF.Price()
    print(df)
    df = PF.PriceSeries()
    print(df)
    
    df = MA_Periods(code)
    df = Return_Periods(code)
    #OH_Periods(code)
    
        