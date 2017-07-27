from ..utils.tradedate import tradedate
import pandas as pd 
from WindPy import w 
w.start()

def allAstock():
    data = w.wset("sectorconstituent", "date="+str(tradedate(0)[1]) , "sectorid = a001010100000000")
    df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
    del df["date"]
    df = df.set_index("wind_code")
    #print(df.head())
    print("All stock Num : {} ".format(len(df)))
    return df

def allMainBoardStock():
    data = w.wset("sectorconstituent", "date="+str(tradedate(0)[1]) , "sectorid=1000007902000000")
    #print(data)
    df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
    del df["date"]
    df = df.set_index("wind_code")
    #print(df.head())
    print("MSCI stock Num : {} ".format(len(df)))
    return df


def MSCIAStock():
    data = w.wset("sectorconstituent", "date="+str(tradedate(0)[1]) , "sectorid=1000027970000000")
    #print(data)
    df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
    del df["date"]
    df = df.set_index("wind_code")
    #print(df.head())
    print("MSCI stock Num : {} ".format(len(df)))
    return df

def HKToChina():
    data = w.wset("sectorconstituent","date="+str(tradedate(0)[1]) ,"sectorid=1000025141000000")
    #print(data)
    df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
    df = df.set_index("wind_code")
    del df['date']
    #print(df.head())
    print("All stock Num : {} ".format(len(df)))
    return df

def HKToSZ():
    data = w.wset("sectorconstituent","date="+str(tradedate(0)[1]) ,"sectorid=1000023475000000")
    #print(data)
    df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
    df = df.set_index("wind_code")
    #print(df.head())
    print("All stock Num : {} ".format(len(df)))
    return df

def HKToSH():
    data = w.wset("sectorconstituent","date="+str(tradedate(0)[1]) ,"sectorid=1000014938000000")
    #print(data)
    df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
    df = df.set_index("wind_code")
    #print(df.head())
    print("HK to shnaghai Num : {} ".format(len(df)))
    return df
