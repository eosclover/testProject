"""
人人网登陆，获取登陆后的信息
"""
import requests

def login():
      url='https://passport.cnblogs.com/user/signin'
      header={'Accept':'application/json, text/javascript, */*; q=0.01',
              'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
              'Content-Type':'application/json; charset=UTF-8',
              'Referer':'https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F'}
      data={
	        "input1": "b7vieiOEvoI1//HNXTlGp7lCkVMjD9L2BovvlZ9IqnvFQDAaW6zH4ilYm5LpxUjoB/tt1bshkWnmeOg9bYZJ0jmcX841ybX0KiUa6KUp530775PTl8rX30Y2DXbxU41TE9X5DusVW8Yxjgxcwr3FCj8hxWJWS1GTkU3gLejmfLY=",
	        "input2": "rWK3p2GWXthmMsdotsNg5tGHe5IibMYaLa/dmgTZDqCcRqu0uG40RbjmFgBgYdOgxI/HZTu38dhvQvM3sxoVrZunQOTyus7oYdzQa2Yt2balHEKkvQulLo1Zee6bDkTj4qAq0G3bcmgdBPUeKtPjaJc2y0CntleGUzjRC0Y+k+M=",
	        "remember": "false",
	        "geetest_challenge": "3f720cd84be6dbcfdc5a4cf1bced5966ds",
	        "geetest_validate": "3d1ebcb46793153bd7691dcb93d5b253",
	        "geetest_seccode": "3d1ebcb46793153bd7691dcb93d5b253|jordan"
                  }
      r=requests.post(url=url,data=data,headers=header)
      # print(r.cookies)
      return r.cookies



def inof():
      url='https://www.cnblogs.com/mvc/blog/news.aspx?blogApp=eosclover'
      header={'Accept':'text/plain, */*; q=0.01',
               'X-Requested-With':'XMLHttpRequest',
              'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
              'Referer':'https://www.cnblogs.com/eosclover/p/6409288.html'}
      para={'Cookie':login()}

      r=requests.get(url=url,params=para,headers=header)
      print(r.text)
inof()
































"""
1.先登录人人网
2.登录成功后获取cookie
# """
# url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201860920896'
# # header = {'Content-Type':'application/x-www-form-urlencoded',
# #         'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
# #         'Referer':'http://www.renren.com/SysHome.do'}
# data={'email': '18310765482',
#       'icode': '',
#       'origURL': 'http://www.renren.com/home',
#       'domain': 'renren.com',
#       'key_id': '1',
#       'captcha_type': 'web_login',
#       'password': '352401b46f94436d5e3824570a5a04ad8179979ec8852d9c9d360f15b358d22d',
#       'rkey': '488c7e70ed9a9ff58385877142a5f294',
#       'f': 'http%3A%2F%2Fzhibo.renren.com%2Ftop'}
# r = requests.post(url=url, data=data)
# # return r.cookies
# print(r.text)
# print(r.cookies)
# #返回
# # login()
# # def info():
# #     """查看信息个人信息"""
# #     url = 'http://www.renren.com/966934817/profile'
# #     header={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
# #             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# #             'Cookie': login()}
# #     r = requests.get(url=url,headers=header)
# #     print(r.text)
# #
# #
# # info()