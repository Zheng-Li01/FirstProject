# https://zhuanlan.zhihu.com/p/36584668

import requests
from bs4 import BeautifulSoup
import bs4
import time
import os
import csv

def get_one_page(url):
    try:
        headers ={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'
        }
        response =requests.get(url =url,headers=headers,timeout =10)
        if response.status_code ==200:
            return response.text
        return None
    except EOFError as e:
        print(e)
        return None

def parse_one_page(html,comment_info):
    soup = BeautifulSoup(html,'html.parser')
    for comments in soup.find_all('div',class_='comment'):
        comment = comments.find('span',class_='short').get_text()
        time = comments.find('span',class_='comment-time').get_text()
        name = comments.find('a').get('href')
        comic={}
        comic['comment'] =comment
        comic['Time']=time
        comic['Name']=name
        # comment_info.append(comic)
        print(comic)

    return comic
    
# def write_to_file(comment_info,time_info, name_info):
#     with open ('TouHaoWanJi.txt','a',encoding='utf-8') as f:
#         f.write(comment_info +'\n')
#         f.write(time_info +'\n')
#         f.write(name_info +'\n')
#         f.write('\n\n')

def write_to_file(comment_info):
    with open ('TouHaoWanJi.csv','a',newline='') as f:
        filednames=['comment','Time','Name']
        writer = csv.DictWriter(f,fieldnames=filednames)
        writer.writeheader()
        try:
            writer.writerows(comment_info)
        except:
            pass

def main(start):
    comment_info={}

    url = 'https://movie.douban.com/subject/4920389/comments?start=' + str(start) + '&limit=20&sort=new_score&status=P&percent_type='
    html = get_one_page(url)
    data = parse_one_page(html,comment_info)
    write_to_file(comment_info)

if __name__ =='__main__':
    for i in range(3):
        main(i*20)
        print('completed the current page')
        time.sleep(1)



