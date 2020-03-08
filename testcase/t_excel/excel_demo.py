#步骤：
#导入包,xlrd
import xlrd
#创建wordbook对象
book = xlrd.open_workbook("testdata.xlsx")
#sheet对象 1索引  2名称
# sheet = book.sheet_by_index(0)
#2
sheet = book.sheet_by_name("Sheet1")
#获取行数和列数
rows = sheet.nrows #行
cols = sheet.ncols#列
#读取每行的内容
for r in range(rows):
    r_values = sheet.row_values(r)
    print(r_values)

#读取每列的内容
for c in range(cols):
    c_values = sheet.col_values(c)
    print(c_values)

#读取固定列的内容
print(sheet.cell(1,1))