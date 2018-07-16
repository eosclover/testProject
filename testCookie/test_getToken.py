"""
患者端登录，查看个人信息详情
"""
import requests
import unittest
import json


class testhzApp(unittest.TestCase):
    def setUp(self):
        print('----------开始了------------')

    def tearDown(self):
        print('----------结束了------------')

    def test_login(self):
        self.url = 'http://XXXX。XX。XX。XX/jzgxp/myinfopatient/login'
        self.header = {'authorization': 'token=b5871a8b005e4ac79db0d69002f83e6f',
                       'device': 'imei=866146036223745',
                       'Content-Type': 'application/json; charset=UTF-8',
                       'Host': 'ylt.gaoxinhealth.com',
                       'Connection': 'Keep-Alive',
                       'Accept-Encoding': 'gzip',
                       'User-Agent': 'okhttp/3.6.0'}
        self.data = {
            "code": "c56d0e9a7ccec67b4ea131655038d604",
            "phone": "183923289XX",
            "type": "1"}
        response = requests.post(url=self.url, json=self.data, headers=self.header)
        print(response.status_code)

        print(response.text)  # string
        millde_result = json.loads(response.text)
        if millde_result['data'] == None:
            print("if")
            print(millde_result['data'])
            return ""
        else:
            print("else")
            print(millde_result['data']['token'])
            return millde_result['data']['token']
            # return str(response.text['data']['token'])
            # return millde_result['data']['token']
            # 98d96db6006245f1bf16c0e6411e8c20

    def myinfo(self):
        self.url = ''
        self.header = ''
        self.data = ''
        r = requests.post()


if __name__ == '__main__':
    unittest.main()
