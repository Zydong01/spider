# https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg1.juimg.com%2F180329%2F330819-1P32913244598.jpg&refer=http%3A%2F%2Fimg1.juimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1642143600&t=d4735439a1d2942c379c177b511e5164
import requests
root = "/home/zydong/下载/"
url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg1.juimg.com%2F180329%2F330819-1P32913244598.jpg&refer=http%3A%2F%2Fimg1.juimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1642143600&t=d4735439a1d2942c379c177b511e5164"
path = root + url[-6:]
try:
    r = requests.get(url)
    print(r.status_code)
    r.raise_for_status()
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
except:
    print("失败")

