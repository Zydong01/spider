import bs4
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")


def fillUnivList(uLIst, html):
    # soup代表html的根节点
    soup = BeautifulSoup(html, "html.parser")
    schoolsNames = soup.find_all("a", "name-cn")
    # print(schoolsNames[0])
    i = 0
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all("td")
            # print(tds[0].string)
            # print(tds[4].string)
            a = tds[0].string
            uLIst.append([tds[0].string, schoolsNames[i].string, tds[4].string])
            i = i + 1
    return uLIst


def printUnivList(uList, num):
    tplt = "{:^10}\t{:^6}\t{:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = uList[i]
        # u[0].string.replace('\n', '').replace("\r", '').replace(' ', '')
        # u[1].string.replace('\n', '').replace("\r", '').replace(' ', '')
        # u[2].string.replace('\n', '').replace("\r", '').replace(' ', '')
        # 只有在format中replace才起作用
        print(tplt.format(u[0].replace('\n', '').replace("\r", '').replace(' ', ''),
                          u[1].replace('\n', '').replace("\r", '').replace(' ', ''),
                          u[2].replace('\n', '').replace("\r", '').replace(' ', ''), chr(12288)))


if __name__ == '__main__':
    url = "https://www.shanghairanking.cn/rankings/bcur/2021"
    uList = []
    num = 20
    html = getHTMLText(url)
    fillUnivList(uList, html)
    printUnivList(uList, num)
