import xlrd

xldata = xlrd.open_workbook(r'F:\selenium_Python\Python\DataDocument\LoginUserData.xlsx')
print(xldata)
sheet = xldata.sheets()[0]
print(sheet.nrows, sheet.ncols)

print(sheet.row_values(0))