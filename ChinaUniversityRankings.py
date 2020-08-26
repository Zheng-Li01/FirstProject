import requests
from bs4 import BeautifulSoup
import bs4
import time

## From https://zhuanlan.zhihu.com/p/36478306.
def get_one_Page(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status() # to assert the statu code of the response is 200 or not
        response.encoding = response.apparent_encoding # Get the accurate code
        return response.text
    except:
        print("Exception appeared")
        return ""

def parse_one_page(ulist,html):
    soup = BeautifulSoup(html,'html.parser') # html.parser is thh lib of python for parse
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            # # print(tds[0])
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
            # print(ulist)

def print_one_page(ulist,num):
    tplt ="{0:^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:^10}" # 0 the orderof location; ^ align middle ; {4} using the chr(122888) to fill， is a usful way for chiese align
    print(tplt.format("排名","学校名称","学校地址","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))

def main():
    uinfo=[]
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = get_one_Page(url)
    parse_one_page(uinfo,html)
    print_one_page(uinfo,1)

if __name__ == '__main__':
    main()
    