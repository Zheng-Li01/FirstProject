# https://zhuanlan.zhihu.com/p/37385870

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import os
import time
from multiprocessing.pool import Pool

def get_one_page(offset,keyword):
    paras ={
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload': 'true',
        'count':20,
        'cur_tab':1,
        'from':'search_tab',
        'aid':24,
        'app_name':'web_search',
        'en_qc':1,
        'pd':'synthesis',
        'timestamp': 1599129430605,
        'signature':'gAYucgAgEBD7ww5sK8RhOIAHb2AAN9kwl0tD9QfUt12.JfkUoqk0sjPjacy6SZczmgItLD67fqx72.2VgFoXXhmo.N1VvWw.FbCroIXTctP7inqrQJFG1CsTsQU2JUGfYsR'

    }

    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(paras)
    
    try:
        response = requests.get(url,timeout =10)
        if response.status_code  ==200:
            # print('successful')
            # print(type(response.text))
            return response.text
        else:
            return None
    except:
        print('failed')
        return None

def parse_one_page(html):
    urls=[]
    data =json.loads(html)
    # print(data)

    if data and 'data_ext' in data.keys():
        print(data.keys())
        for item in data.get('data_ext'):
            page_urls=[]
            title = item.get('title')
            print(title)
            print(type(item))
            image_detail = item.get('image_list')
            print(image_detail)
            print(type(image_detail))
            for i in range(len(image_detail)):
                url = image_detail[i]['url']
                page_urls.append(url)
            urls.append({'title':title,'url_list':page_urls})
    return urls

def save_image_file(urls):
    count =0
    file_dir ='C:/Users/v-zhgl/source/repos/FirstProject/PictureFromJRTT'
    for item in urls:
        file = file_dir + item['title']
        if os.path.exists(file):
            os.chdir()
        else:
            os.mkdir(file)
            os.chdir(file)
        for n in item['url_list']:
            response = requests.get('http:'+n)
            if response.status_code ==200:
                file_path = item['title'] +'('+str(count) + ')'+'.jpg'
                count +=1
                print(file_path)

                if not os.path.exists(file_path):
                    with open (file_path,'wb') as f:
                        f.write(response.content)
                        print('successfully')
                        time.sleep(2)
                else:
                    print('done')
        count =0

def main(offset,word):
    html =get_one_page(offset,word)
    # print(html)
    urls = parse_one_page(html)
    save_image_file(urls)

if __name__ =="__main__":
    # pool = Pool()
    # grooups =([i *20 for i in range(2)])
    # pool.map(main('街头篮球'),grooups)
    # pool.close()
    # pool.join()
    for i in range(2):
        main(i *20,'篮球')
