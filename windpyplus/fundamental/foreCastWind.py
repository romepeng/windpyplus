import pandas as pd
from datetime import datetime, date, timedelta
from windpyplus.utils.tradedate import tradedate
from WindPy import w
w.start()

def foreCastWind(stocklists, reportDate = '20170930'):  
    data = w.wss(stocklists, 
        "sec_name,profitnotice_style,profitnotice_lasteps,profitnotice_changemax,profitnotice_changemin,profitnotice_date,profitnotice_abstract,profitnotice_netprofitmin,profitnotice_netprofitmax,",
        "rptDate=" + str(reportDate))
    # stm_predict_issuingdate
    df = pd.DataFrame(data.Data, columns=data.Codes, index=data.Fields).T
    #df = df[df['PROFITNOTICE_CHANGEMIN'] > -10]
    #df['PROFITNOTICE_NETPROFITMEAN'] = 0.5*(df['PROFITNOTICE_CHANGEMIN'] + df['PROFITNOTICE_NETPROFITMAX'])
    # PROFITNOTICE_DATE,  STM_PREDICT_ISSUINGDATE
    df = df[df['PROFITNOTICE_DATE'] > (datetime.now() + timedelta(days=-150))]
    df = df.sort_values(by= 'PROFITNOTICE_DATE', ascending=False)
    df['PROFITNOTICE_CHANGEMEAN'] = 0.5*(df['PROFITNOTICE_CHANGEMIN'] + df['PROFITNOTICE_CHANGEMAX'])
    df['PROFITNOTICE_DATE'] =  df['PROFITNOTICE_DATE'].apply(lambda x: x.date())
    #df['STM_PREDICT_ISSUINGDATE'] = df['STM_PREDICT_ISSUINGDATE'].apply(lambda x:x.date())
    print(df[df['PROFITNOTICE_DATE'] == date.today()])
    print('NUM of PROFITNOTICE LIST :{}'.format(len(df)))
    return df




