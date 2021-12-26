import requests


def getHTML_Text(url, keyword):
    kv = {'wd': keyword}
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()
        print(r.status_code)
        print(r.request.url)
        print(r.text)
    except:
        print("失败")


if __name__ == '__main__':
    url = "http://www.baidu.com/s"
    keyword = 'python'
    getHTML_Text(url, keyword)
