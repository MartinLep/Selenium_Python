import xlsxwriter

xl = xlsxwriter.Workbook(r'F:\selenium_Python\Python\DataDocument\Martin.xls')
sheet = xl.add_worksheet('Martin')
sheet.write_string(0, 0, 'username')
sheet.write_string(0, 1, 'password')
sheet.set_column('A:B', 30)
xl.close()


