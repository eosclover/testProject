"""
患者端登录，查看个人信息详情
"""
import requests
import unittest
import json
from testProject.HMTC_HZAPP.testCase import getToken


class testhzApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('----------开始了------------')

    @classmethod
    def tearDownClass(cls):
        print('----------结束了------------')


    def test_mydoc(self):
        url = 'http://ylt.gaoxinhealth.com/jzgxp/attdoctor/myFocusDocs'
        # getToken.test_login_getToken()
        header = {'authorization':'b98e9d3347e848e7a66dbdae2f09b5f6',
              'device': 'imei=866146036223745'}
        r = requests.get(url=url, headers=header)
        print(r.json())
        self.assertEqual(r.json()['data']['nmDoctor'], '赵清风')


if __name__ == '__main__':
    unittest.main()
