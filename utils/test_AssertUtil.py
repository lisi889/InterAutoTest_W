from utils.LogUtil import my_log
import json

class AssertUtil:
    #初始化数据、日志
    def __init__(self):
        self.log = my_log("AsserUtil")
    #code相等
    def assert_code(self,code,expexted_code):
        try:
            assert int(code) == int(expexted_code)
            return True
        except:
            self.log.error("code error is %s,expexted_code is %s" % (code,expexted_code))
            raise
    #body相等
    def assert_body(self,body,expexted_body):
        try:
            assert body == expexted_body
            return True
        except:
            self.log.error("body error,body is %s,expexted_body is %s" % (body,expexted_body))
            raise
    # body包含
    def assert_in_body(self,body,expexted_body):
        try:
            #转json
            body = json.dumps(body)
            assert expexted_body in body
            return True
        except:
            self.log.error("expexted_body not in ,body is %s, expexted_body is %s" % (body,expexted_body))
            raise