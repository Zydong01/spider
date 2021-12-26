# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=7&p4ppushleft=2%2C48&ntoffset=7&s=0

# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&p4ppushleft=2%2C48&ntoffset=4&s=44

# https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=1&p4ppushleft=2%2C48&ntoffset=1&s=88

# 观察上述每页商品的url，最后的数字相当于当前页商品的起始序号

# 淘宝和京东商品的爬取方法有点区别：京东的页面排版类似于最好大学程序的实现，而淘宝的商品排版是一个很长的字符串

import requests
from bs4 import BeautifulSoup
import re


def getHTMLText(url):
    try:
        kv = {"user-agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


'''
网页示例：商品价格部分
		<div class="p-price">
							<strong class="J_100008072005" data-presale="0"  data-done="1"  >
									<em>￥</em><i data-price="100008072005">79.00</i>
							</strong>
						</div>
'''


def parserHtml(html):
    soup = BeautifulSoup(html, "html.parser")
    goodsPrice = soup.find_all(name="i", attrs={"data-price": re.compile("^‐?\d+$")})
    goodsName = soup.find_all("div", "p-name p-name-type-2")
    # str = "".join(goodsName)
    # match = re.search(r'^<em>$', goodsName)
    # if match:
    #     print(match)

    # print(goodsPrice)
    print(len(goodsName))
    for i in range(len(goodsName)):
        print(goodsName[i])
    return ""


def printGoods(goodsList):
    ""


if __name__ == '__main__':
    url = "https://search.jd.com/Search?keyword=书包"
    goodsList = []
    html = getHTMLText(url)
    parserHtml(html)
    printGoods(goodsList)
