import os

from config import Conf
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
#获取测试用例list
#获取testlogin.yml文件路径
test_file = os.path.join(Conf.get_data_path(),"testlogin.yml")
# print("-----test---",test_file)
#使用工具类来读取多个文档内容
data_list = YamlReader(test_file).data_all()
# print("-----test---",data_list)
#参数化执行测试用例

@pytest.mark.parametrize("login",data_list)
def test_yaml(login):
    #初始化url,data
    url = ConfigYaml.get_conf_url()+login["url"]
    # print("-----test---",url)

    data = login["data"]
    print("data%s",data)
    #post请求
    request = Request()
    res= request.get()
    print(res)

if __name__ == "__main__":
    pytest.main(["-s","test_login.py"])