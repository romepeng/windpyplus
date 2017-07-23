from datetime import datetime, timedelta
from WindPy import w
w.start()

def tradedate(days=30):
    lastdate = datetime.now().date()
    starttradedate = (datetime.now() - timedelta(days)).date()
   
    if lastdate.weekday() == 5 or lastdate.weekday() == 6:
        lasttradedate = w.tdaysoffset(0, lastdate).Data[0][0].date()
    else:
        lasttradedate = w.tdaysoffset(-1, lastdate).Data[0][0].date()
    if starttradedate >= lasttradedate:
        starttradedate = lasttradedate
    else:
        pass
    return (str(starttradedate), str(lasttradedate))


def futuredate(days=30):
    lastdate = datetime.now().date()
    futuredate = datetime.now().date()  + timedelta(days)
    futuretradedate = w.tdaysoffset(0, futuredate).Data[0][0].date()
    return (str(lastdate), str(futuredate), str(futuretradedate))



