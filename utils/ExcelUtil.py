#目的：参数化、pythest、list
import os

import xlrd
# from testcase.t_excel.excel_demo import sheet
#自定义异常

class SheetTypeError:
    pass


class ExcelReader:
#验证文件是否存在
    def __init__(self,excel_file,sheet_by):
        # print(excel_file,sheet_by)
        # print(os.path)
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise FileNotFoundError
#读取sheet方式，名称、索引
    def data(self):
        # 存在就读取不存在就不读取
        if not self._data:
            workbook = xlrd.open_workbook(self.excel_file)
            if type(self.sheet_by) not in[str,int]:
                raise SheetTypeError("请输入ｉnt　or str")
            elif type(self.sheet_by) ==int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)
    #读取sheet内容
        #返回ｌｉｓｔ　　元素：字典
        #获取首行信息
            title = sheet.row_values(0)
            #遍历测试行和值，组成ｄｉｃｔ,放在ｌｉｓｔ

            for col in range(1,sheet.nrows):
                #获取ｖａｌｕｅｓ
                col_values = sheet.row_values(col)
                self._data.append(dict(zip(title,col_values)))

#结果返回
        return self._data

if __name__ == "__main__":
    reder = ExcelReader("../data/testdata.xlsx","Sheet1")
    print(reder.data())