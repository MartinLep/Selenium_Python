import time
import xlsxwriter

class Loginloginfo(object):
    def __init__(self, path='', mode='w'):
        fname = path+time.strftime('%Y-%m-%d', time.gmtime())
        self.log = open(path+fname+'.text', mode)
    def log_write(self, loginfo):
        self.log.write(loginfo)
    def log_close(self):
        self.log.close()

class XLLoginfo(object):
    def __init__(self, path = '', mode = ''):
        fname = path + time.strftime('%Y-%m-%d', time.gmtime())
        self.row = 0
        self.xl = xlsxwriter.Workbook(path+fname+'.xls')
        self.style=self.xl.add_format({'bg_color':'red'})

    def xl_write(self, *args):
        col = 0
        style = ''
        if 'error' in args:
            style = self.style
        for val in args:
            self.sheet.write_string(self.row, col, val, style)
            col += 1
        self.row += 1
    def XL_init(self, sheetname, *title):
        self.sheet = self.xl.add_worksheet(sheetname)
        self.sheet.set_column('A:E', 30)
        self.xl_write(*title)
    def XL_Write(self, *args):
        self.xl_write(*args)
    def XL_Close(self):
        self.xl.close()

if __name__ == '__main__':
    log = Loginloginfo()
    log.log_write('seleniumTest')
    log.log_close()