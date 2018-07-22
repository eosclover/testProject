import requests
url='http://www.baidu.com'

res=requests.get(url=url)
print(res.text)