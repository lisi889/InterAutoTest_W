#导入yaml
import yaml
#读取单个文档save_load
# with open("./data.yml","r",encoding="utf8") as f:
#     #读取yaml文件
#     r = yaml.safe_load(f)
# #输出
# print(r)

from utils.YamlUtil import YamlReader
res = YamlReader("./data.yml").data()
#多个
# res = YamlReader("./data_all.yml").data_all()
print(res)
