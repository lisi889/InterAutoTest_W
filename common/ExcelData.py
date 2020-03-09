from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig
class Data:
    def __init__(self,tesecase_file,sheet_name):
        #使用ｅｘｃｅｌ工具类，获取结果ｌｉｓｔ
        # self.reder = ExcelReader("../data/testdata.xlsx", "Sheet1")
        self.reder = ExcelReader(tesecase_file,sheet_name)
        # print(self.reder.data())

    def get_run_data(self):
        # 列是否运行内容ｙ
        run_list = []
        for line in self.reder.data():

            if str(line[DataConfig.is_run]).lower() == "y":
                print(line)
                #保存执行的结果放到新列表
                run_list.append(line)
        print(run_list)
        #保存要执行的结果，放到新的列表
        return run_list