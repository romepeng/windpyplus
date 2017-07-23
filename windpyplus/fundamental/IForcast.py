import pandas as pd
from windpyplus.utils.tradedate import tradedate
from datetime import datetime
from WindPy import w 
w.start()

def iForecast(code, startdate = tradedate(180)[0], year = datetime.strptime(tradedate(0)[1],"%Y-%m-%d").year):
    data = w.wset("institutionforecasts", "year=" + str(year), "startdate=" +startdate, "windcode=" +code ,"orgname=all")
    #print(data)
    df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
    #print(df.head())
    df = df.sort_values(by ='last_rating_date', ascending = False)
    return df

def stockWest(code,startdate = tradedate(180)[0], year = datetime.strptime(tradedate(0)[1],"%Y-%m-%d").year):
    data = w.wset("stockwest",
        "startdate=" + startdate, "windcode=" + code ,"orgname=全部",
        "field=date,organization,researcher,epsa0,epse1,epse2,epse3,netprofita0,netprofite1,netprofite2,netprofite3,incomea0,incomee1,incomee2,incomee3")
    #print(data)
    df = pd.DataFrame(data.Data, index= data.Fields, columns=data.Codes).T
    df = df.sort_values(by ='date', ascending = False)
    return df
    
if __name__ == '__main__':
    df = iForecast('000333.SZ')
   
    print(df)
    from windpyplus.utils.dfToExcel import dfToExcel
    dfToExcel(df, "iForecast_code")
    df = stockWest('002139.sz')
    print(df)
