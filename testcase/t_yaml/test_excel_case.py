import json
import re

import allure

from config import Conf
from config.Conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.EmailUtil import SendEmail

from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Request
from common import Base
import pytest
from utils.AssertUtil import AssertUtil

#初始化
#初始化测试用例文件
# case_file = os.path.join("../data/",ConfigYaml().get_excel_file())
case_file = os.path.join("../../data/testdata.xlsx")
# print("------------",case_file)
#测试用例sheet名称
# sheet_name = ConfigYaml().get_excel_sheet()
sheet_name = "Sheet1"
# print(sheet_name)
#获取测试用例列表
data_init = Data(case_file,sheet_name)
run_list = data_init.get_run_data()

# print("---test----",run_list)
# 日志
log = my_log()
#初始化data_config
data_key = ExcelConfig.DataConfig
#编写测试用例方法  参数化运行
#一个用例的执行
class TestExcel:

    def run_api(self,url,method,params=None,header=None, cookie=None):
        """发送请求api"""
        # 接口请求
        request = Request()
        # params转义json
        if len(str(params).strip()) is not 0:
            params = json.loads(params)
        # method post、get
        if str(method).lower() == "get":
            # 增加了headers
            res = request.get(url, json=params, headers=header, cooikes=cookie)
        elif str(method).lower() == "post":
            res = request.post(url, json=params, headers=header, cooikes=cookie)
        else:
            log.error("错误的请求method %s" % method)
        # print(res)
        return res

    # 增加pytest
    def run_pre(self,pre_case):
        """初始化数据"""
        url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params_type = pre_case[data_key.params_type]
        params = pre_case[data_key.params]
        expect_result = pre_case[data_key.expect_result]
        headers = pre_case[data_key.headers]
        cooikes = pre_case[data_key.cookies]


        # 判断header是否存在，json转义
        # if headers:
        #     header = json.loads(headers)
        # else:
        #     header = headers
        header = Base.json_parse(headers)
        # 判断cooikes是否存在，json转义
        # if cooikes:
        #     cooike = json.loads(cooikes)
        # else:
        #     cooike = cooikes
        cooikes = Base.json_parse(cooikes)
        res = self.run_api(url, method, params, headers)
        print("前置用例执行：%s" % res)
        return res


    # 初始化信息，url,data
    # 修改方法参数
    @pytest.mark.parametrize("case", run_list)
    def test_run(self,case):
        # print("-----------------",case)
        # 重构函数内容
        # data_key = ExcelConfig.DataConfig
        #run_list 第1个用例，key获取values
        url = ConfigYaml().get_conf_url()+case[data_key.url]
        print("----------",url)
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        headers = case[data_key.headers]
        cooikes = case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]
        #接口请求


        #验证前置条件：
        if pre_exec:
            pass
        #找到执行用例
        # 前置测试用例
            pre_case = data_init.get_case_pre()
            print("前置条件信息为%s" % pre_exec)
            pre_res = self.run_pre(pre_case)
            headers, cooikes = self.get_correlation(headers,cooikes,pre_res)

        header = Base.json_parse(headers)
        cooikes = Base.json_parse(cooikes)
        res = self.run_api(url, method, params, headers,cooikes)
        print("测试用例执行：%s" % res)
        # #接口请求
        # request = Request()
        # #params转义json
        # if len(str(params).strip()) is not 0:
        #     params = json.loads(params)
        # #method post、get
        # if str(method).lower() == "get":
        #     #增加了headers
        #     res = request.get(url, json=params,headers = header,cooikes=cookie)
        # elif str(method).lower() == "post":
        #     res = request.post(url, json=params,headers = header,cooikes=cookie)
        # else:
        #     log.error("错误的请求method %s" % method)
        # print(res)

        #allure
        #sheet名称  feature一级标签
        allure.dynamic.feature(sheet_name)
        #模块   story 二级标签
        allure.dynamic.story(case_model)
        #用例ID+接口名称  title
        allure.dynamic.title(case_id+case_name)
        #请求url  请求类型  期望结果   实际结果描述
        desc = "<font color = 'red'>请求URL：</font>{}<br/>" \
               "<font color = 'red'>请求类型：</font>{}<br/>" \
               "<font color = 'red'>期望结构：</font>{}<br/>" \
               "<font color = 'red'>实际结果：</font>{}".format(url,method,expect_result,res)
        allure.dynamic.description(desc)



# TestExcel().test_run()
        #断言验证
        #状态码

        assert_util = AssertUtil()
        assert_util.assert_code(int(res["code"]),int(code))
        #返回结果内容
        assert_util.assert_in_body(res["body"],str(expect_result))
        #数据库结果断言
        #初始化数据库
        Base.assert_db("db_1",res("body"),db_verify)
        from common.Base import init_db
        # sql = init_db("db_1")
        # #查询sql，excel定义好的
        # db_res = sql.fechone(db_verify)
        # log.debug("数据库查询结果：{}".format(str(db_res)))
        # #数据库的结果与接口返回的结果验证
        # #获取数据库的结果key
        # verify_list = list(dict(db_res).keys())
        # #根据key获取数据库的结果，接口的结果
        # for line in verify_list:
        #     res_line = res["body"][line]
        #     res_db_line = dict(db_res)[line]
        # #验证
        # assert_util.assert_body(res_line,res_db_line)
#关联方法
    def get_correlation(self, headers,cookies,pre_res):
        """
        验证是否有关联
        有关联执行前置用例获取结果
        结果的替换
        :return:
        """
        #验证是否关联
        headers_para, cookies_para = Base.params_find(headers,cookies)
        #有关联，执行前置用例，获取结果
        if len(headers_para):
            headers_data = pre_res["body"][headers_para[0]]
            # 替换结果
            headers = Base.res_sub(headers, headers_data)
        if len(cookies_para):
            cookies_para = pre_res["body"][cookies_para[0]]
            #替换结果
            cookies = Base.res_sub(headers, cookies_para)
        return headers,cookies


if __name__ =="__main__":
    # report_path = Conf.get_report_path()+os.sep+"result"
    # report_html_path = Conf.get_report_path()+os.sep+"html"
    # pytest.main(["-s","test_excel_case.py","--alluredir",report_path])

    Base.allure_report(report_path,report_html_path)
    # Base.allure_report("./report/result","./report/html")
    Base.send_mail(title="接口测试报告结果",content = report_html_path)
    #替换header变量
    #验证请求中是否${},返回${}$内容，
    # str1 = '{"Aythorization":"JWT ${token}$"}'
    # if "${" in str1:
    #     print(str1)
    # import re
    # patten = re.compile('\${(.*)}\$')
    # re_res = patten.findall(str1)
    # print(re_res[0])
    # # 根据内容token查找前置条件测试用例返回结果,
    # token = "123"
    # # 根据变结果内容进行替换
    # res = re.sub(patten,token,str1)
    # print(res)

    #发送请求