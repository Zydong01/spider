import requests


def getHTML_Text(url):
    try:
        kv = {"user-agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv)
        # r = requests.get(url)
        r.raise_for_status()
        # 如果加上r.raise_for_status()，返回状态码出现异常，会直接跳到except捕获异常；不加的话，会继续执行
        r.encoding = r.apparent_encoding
        print(r.request.headers)
        print(r.status_code)
        print(r.text)
    except:
        print("爬取失败")


if __name__ == '__main__':
    url = "https://www.amazon.cn/dp/B08XPC9WS4/ref=s9_acsd_hps_bw_c2_x_0_i?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-1&pf_rd_r=1H865135B59899P8D5FS&pf_rd_t=101&pf_rd_p=b2083751-6bce-4f44-9ee3-670202db1b4e&pf_rd_i=2108199071"
    getHTML_Text(url)
