from windpyplus.utils.tradedate import tradedate
import pandas as pd

def dfToExcel(df, filename, sheet_name=tradedate(0)[-1]):
    df.to_excel("D:/Stock/wind/" + str(filename) + ".xlsx", sheet_name)
    print(" df save to {} .".format(filename))

def dftoSameWorkbook(df_lists, sheetName_lists, filename):
    writer = pd.ExcelWriter(filename)
    for i in range(len(df_lists)):
        df_lists[i].to_excel(writer, sheetName_lists[i])
    writer.save()
    print(" multiple df save to {} .".format(filename))

