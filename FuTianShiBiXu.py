# From https://zhuanlan.zhihu.com/p/36506024
import os
import bs4
import requests
import tqdm
import time
from bs4 import BeautifulSoup


def get_one_page(all_url):
    """get the signle page's html text"""
    try:
        response = requests.get(all_url,timeout=30)
        response.raise_for_status()
        response.encoding =response.apparent_encoding
        # print(response.text)
        return response.text
    except:
        print("failed")
        return None

def parse_all_pages(html, urls,chapter_name):
    '''parse the html & saved to the list'''
    soup = BeautifulSoup(html,'html.parser')
    chapters = soup.find('div', class_='listmain')
    for dd in chapters.find_all('a')[12:]:
        urls.append(dd.get('href'))
        chapter_name.append(dd.text)

def parse_one_chapter(content):
    soup = BeautifulSoup(content,'html.parser')
    # title = soup.find('div',class_='content').find('h1').text
    texts= soup.find_all('div',class_='showtxt')[0].text
    return texts


def write_to_file(chapter_name,texts):
    with open('FuTianShi.txt','a',encoding='utf-8') as  f:
        f.write(chapter_name +'\n')
        f.write(texts)
        f.write('\n\n')

def main():
    urls =[] # to save the links
    chapter_name =[] # to save the chapter name
    all_url ="https://www.biqukan.com/2_2412/"
    html = get_one_page(all_url)
    parse_all_pages(html,urls,chapter_name)
    print("Star DownLoad")
    for i in range(len(chapter_name)):
        url = "https://www.biqukan.com/" + urls[i]
        content = get_one_page(url)
        texts = parse_one_chapter(content)
        write_to_file(chapter_name[i],texts)
        time.sleep(1)
    print("Download completted")

if __name__=='__main__':
    main()
# get_one_page("https://www.biqukan.com/2_2412/")