import yaml
import os
#1创建类
class YamlReader:
#2初始化
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None
#3单个读取
    def data(self):
        if not self._data:
            # print('--test---',self.yamlf)
            # with open("./data.yml", "r", encoding="utf8") as f:
            with open(self.yamlf,"r",encoding="utf8") as f:
            # with open(r"C:\Users\lisi8\PycharmProjects\InterAutoTest_W\config\conf.yml","r",encoding="utf8") as f:
                self._data = yaml.safe_load(f)
        return self._data
#多个读取
    def data_all(self):
        if not self._data_all:
            # with open("./data_all.yml","r",encoding="utf8") as f:
            with open(self.yamlf, "r", encoding="utf8") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all