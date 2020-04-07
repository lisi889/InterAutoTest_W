import requests
#运行log
from utils.LogUtil import my_log
"""第一步封装"""
def requeests_get(url,json):
    r = requests.get(url,json)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text

    res = {}
    res['code'] = code
    res['body'] = body
    return res

"""第二步定义公共方法"""
class Request:
    #初始化log
    def __init__(self):
        self.log = my_log("request")
    def requests_api(self, url,json =None,headers = None, method="get"):
        if method == "get":
            #打印log
            self.log.debug("发送get请求")
            r = requests.get(url, json)
        if method == "request":
            r = r = requests.post(url, json=json, headers = headers)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text

        res = {}
        res['code'] = code
        res['body'] = body
        return res

    """第三步get方法重构"""
    def get(self,url, **kwargs):
        return self.requests_api(url, method="get", **kwargs)



