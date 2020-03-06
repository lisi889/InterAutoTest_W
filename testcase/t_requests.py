import requests
from utils.RequestsUtil import requeests_get
from config.Conf import ConfigYaml
import pytest
#登录post
"""
def login():
    url = "http://211.103.136.242:8064/authorizations"
    data = {"username":"python","password":"12345678"}

    r = requests.post(url,json=data)

    print(r.text)
"""
#获取商品列表get
def test_good_list():
    # url = "http://211.103.136.242:8064/categories/115/skus"  #---使用配置文件的url了
    #定义测试数据
    url_y = ConfigYaml()
    url_path = url_y.get_conf_url()
    url = url_path + "/categories/115/skus"

    data = {
        "page":"1",
        "page_size":"10",
        "ordering":"create_time"
    }
    # r = requests.get(url,json=data)
    r = requeests_get(url,json=data)

    from utils.RequestsUtil import request
    request = request()
    r = request.get(url,json=data)
    # print(r.json())
    print(r)

"""
XHPK7Tg8517DTESltHOhR4J5Us01v9q8MGGYV6y8RhZsluXwbiauqaeqeZCjsAGh
"""
"""
#购物车post
def cart():
    url = "http://211.103.136.242:8064/cart"
    data = {
        "sku_id":"3",
        "count":"1",
        "selected":"true"
    }
    token = "XHPK7Tg8517DTESltHOhR4J5Us01v9q8MGGYV6y8RhZsluXwbiauqaeqeZCjsAGh"
    headers = {
        'Authorizations':'JWT'+ token
    }
    r = requests.post(url, json=data, headers = headers)

    print(r.json())
"""
if __name__=="__main__":
    # login()
    test_good_list()
    # cart()
    # pytest.main(["-s","t_requests.py"])
