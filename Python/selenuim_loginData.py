import codecs
import xlrd
def get_loginfo(path):
    log_info = {}
    config = codecs.open(path, 'r', 'utf-8')
    for line in config:
        result = [ele.strip() for ele in line.split('=')]
        log_info.update(dict([result]))
    return log_info

def get_loginuserdata(path):
    info_array = []
    config = codecs.open(path, 'r', 'utf-8')
    for line in config:
        user_dict = {}
        result = [ele.strip() for ele in line.split(' ')]
        for res in result:
            account = [ele.strip() for ele in res.split('=')]
            user_dict.update(dict([account]))
        info_array.append(user_dict)
    return info_array

class XLUserInfo(object):
    def __init__(self,path=''):
        self.xl = xlrd.open_workbook(path)

    def floattostr(self, val):
        if isinstance(val, float):
            val = str(int(val))
        return val

    def get_sheet_info(self):
        listkey = ['url', 'username', 'password']
        infolist = []
        for row in range(1, self.sheet.nrows):
            info = [self.floattostr(val) for val in self.sheet.row_values(row)]
            tmp = zip(listkey, info)
            infolist.append(dict(tmp))
        return infolist

    def get_sheetinfo_by_name(self, name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheetinfo_by_index(self, index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()

if __name__ == '__main__':
    xinfo = XLUserInfo(r'F:\selenium_Python\Python\DataDocument\LoginUserData.xlsx')
    info = xinfo.get_sheetinfo_by_index(0)
    print(info)
    print(xinfo.get_sheetinfo_by_name('Sheet1'))

# 0-空 1-str 2-num 3-data 4-boolean 5-error
#xl.sheets()[0] 通过索引获取工作表
#table.row_values(0)获取第一行内容
#table.col_values(0)获取第一列内容
# table.nrows行数
# table.ncols列数
# table.cell(0,0).value 单元格的值