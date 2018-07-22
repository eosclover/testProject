import requests
import json


def test_login_getToken():
    url = 'http://ylt.gaoxinhealth.com/jzgxp/myinfopatient/login'
    header = {'Authorization': 'token=null',
              'device': 'imei=866146036223745',
              'Content-Type': 'application/json',
              'cache-control': 'no-cache',
              'Postman-Token': 'cca9bc23-70d6-478d-ba47-b6aa1ff8fa5d',
              'User-Agent': 'PostmanRuntime/7.1.1',
              'Accept': '*/*',
              'Host': 'ylt.gaoxinhealth.com',
              'cookie': 'route=f61b90f94aa3f1aa9e9bb7bd070d8c6a',
              'accept-encoding': 'gzip, deflate',
              'content-length': '90',
              'Connection': 'keep-alive'
              }
    data = {
        "code": "c56d0e9a7ccec67b4ea131655038d604",
        "phone": "18392328987",
        "type": "1"
    }
    print(type(data))
    # reqBody = json.dumps(data)
    # print(reqBody)
    response = requests.post(url,headers=header,data=json.dumps(data))

    # headers = header,
    print(response.text)
    # res=json.loads(response.json())headers=header,
    # print(res)
    # return res['data']['token']


test_login_getToken()
