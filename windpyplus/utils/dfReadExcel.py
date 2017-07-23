import pandas as pd
from windpyplus.utils.dfToExcel import dfToExcel
def readExcel(filename, sheet_name):
    
    xls = pd.ExcelFile(filename)
    try:
        sheet_name = xls.parse(str(sheet_name))
        print(sheet_name.head())
        return sheet_name
    except Exception:
        print("No sheetname {}".format(sheet_name))
    

if __name__ == '__main__':
    df = readExcel("D:/Stock/wind/value5Y_20170508.xlsx", "Wind_20170508")
    print(df.head())
    dfToExcel(df,"value5Y_201705")
