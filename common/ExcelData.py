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
                # print(line)
                #保存执行的结果放到新列表
                run_list.append(line)
        # print(run_list)
        #保存要执行的结果，放到新的列表
        return run_list
    def get_case_list(self):
        """获取全部的测试用例"""
        # run_list = list()
        # for line in self.reder.data():
        #         # print(line)
        #         # 保存执行的结果放到新列表
        #         run_list.append(line)
                # print(run_list)
                # 保存要执行的结果，放到新的列表

        #改用列表推到
        run_list = [line for line in self.reder.data()]
        return run_list
    def get_case_pre(self, pre):
        """获取全部用例
        根据前置条件从全部中取对应的测试用例"""
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None

# if __name__ == "__main__":
#     # ../data/testdata.xlsx Sheet1
#     # <module 'ntpath' from 'C:\\Users\\lisi8\\AppData\\Local\\Programs\\Python\\Python36\\lib\\ntpath.py'>
#     Data("../data/testdata.xlsx","Sheet1")