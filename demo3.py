import requests

url = "https://site.ip138.com/www.baidu.com/"

kv = {"user-agent": "Mozilla/5.0"}
r = requests.get(url, headers=kv)
print(r.request.headers)
print(r.status_code)
print(r.text)