# https://zhuanlan.zhihu.com/p/36761239

import requests
from bs4 import BeautifulSoup

def get_page(url):
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        print('Failed')
        return None

def parse_page(html):
    soup = BeautifulSoup(html,'html.parser')
    part = soup.find('ul',class_='Mean_part__1RA2V')
    print(part)
    print(type(part))
    if part == None:
        print('The word is not exist, please check it again:')
    else:
        meanings =  part.find_all('li')
        for i in range(len(meanings)):
            translations = meanings[i].get_text()
            print(translations)
            print(translations.strip())
            print(''.center(20,'='))

def main():
    while True:
        base_url='http://www.iciba.com/word?w='
        word = input('Please input what you want to check(inout a to exit):')
        if word ==' ':
            print('Input cannot be null')
            continue
        elif word== 'q':
            break
        else:
            url = base_url + word
            print(url)
        html = get_page(url)
        parse_page(html)

if __name__ =='__main__':
    main()


