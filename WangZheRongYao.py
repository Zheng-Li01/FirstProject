# https://zhuanlan.zhihu.com/p/37024324

import requests
from bs4 import BeautifulSoup
import os
import time

file_dir = "C:/Users/v-zhgl/source/repos/FirstProject/ScanForHero/"
url = 'https://pvp.qq.com/web201605/js/herolist.json'

response = requests.get(url)
herolist = response.json()
hero_number = len(herolist)
# print(herolist)
# print(hero_number)

hero_code = herolist[0]['ename'] # 获取英雄编号
hero_name = herolist[0]['cname'] # 获取英雄名称
skin_name = herolist[0]['skin_name'].split('|') # 获取英雄皮肤列表
# print(hero_name)
# print(skin_name)


# for i in range(hero_number):
#     # if herolist[i]['skin_name']:
#     #     skin_name = herolist[i]['skin_name'].split('|')
#     #     print(skin_name)
#     # print(herolist[i])
#     # print(herolist[i].get('skin_name'))
#     print(herolist[i].setdefault('skin_name','Testing'))
#     # print(type(herolist[i]))
#     hero_name = herolist[i]['cname']

for i in range(hero_number):
    hero_name = herolist[i]['cname']
    # print(hero_name)
    # print(type(hero_name))
    skin_name = herolist[i].setdefault('skin_name','Testing').split('|')
    # print(type(skin_name))
    hero_code = herolist[i]['ename']
    # print(hero_code)
    # print(type(hero_code))
    files = file_dir + hero_name
    # print(files)
    if os.path.exists(files):
        os.chdir(files)
    else:
        os.mkdir(files)
        os.chdir(files)

    for j in range(len(skin_name)):
        file_name = hero_name + '-'+ skin_name[j] +'.jpg'
        # print(hero_code)
        skin_url= 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(hero_code) + '/' + str(hero_code) + '-bigskin-' + str(j+1) + '.jpg'
        # skin_url= 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(hero_code) + '/' + str(hero_code) + '-bigskin-' + str(j+1) + '.jpg'
        resonse_skin = requests.get(skin_url)
        time.sleep(2)
        print(resonse_skin.status_code)
        if resonse_skin.status_code == 200:
            with open(file_name,'wb') as f:
                f.write(resonse_skin.content)
