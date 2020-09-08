from lxml import etree
import requests
import os

def get_url_page(url):
    headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    response = requests.get(url, headers = headers, timeout =10)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding # Get teh encode from web site
        # print(response.text)
        return response.text
    else:
        print('Failed to get data')

def parse_url_paget(html):
    image_url=[]
    html_lxml=etree.HTML(html) # get the last partical of links of image
    # print(html)
    links = html_lxml.xpath('//tr//ul/li/a/@href')
    # print(links)
    # print(type(links))
    for link in links:
        if link.endswith('html'):
            image_link='http://www.wallcoo.com'+link
            # print(image_link)
            image_url.append(image_link)
    return image_url

def load_Image(image_info):
    for image_link in image_info:
        # print(image_link)
        html = get_url_page(image_link)
        image_lxml=etree.HTML(html)
        # print(image_lxml)
        image_urls = image_lxml.xpath('//*[@id="thums"]/ul/li/a/img')
        # print(type(image_urls))
        # print(image_urls)
        for image_url in image_urls:
            # print(image_url)
            image_url1 = image_url.attrib['src']
            titles = image_url.attrib['title']
            # print(Title)
            # print(image_url)
            image = image_link[:-10]+image_url1
            # # print(image)
            with open('C:/Users/v-zhgl/source/repos/FirstProject/MaoMaoBiZhao.txt','a',encoding='utf-8') as f:
                f.write(titles+'\t'+image +'\n')
                # f.write(image +'\n')
# response =get_url_page('http://www.wallcoo.com/new/index.html')
# parse_url_paget(response)

def main():
    image_info =[]
    beginPage =0
    endPage =1
    for page in range(beginPage,endPage +1):
        if page ==0:
            url = 'http://www.wallcoo.com/new/index.html'

        else:
            url = 'http://www.wallcoo.com/new/index' + str(page) + '.html'
        html = get_url_page(url)
        image_info = parse_url_paget(html)
        load_Image(image_info)
        
if __name__== "__main__":
    main()





















































































































# text = """
# <div>
# <ul>
# <li class="item_0"><a href=link1.html">First item</a></li>
# <li class="item_1"><a href=link2.html">Second item</a></li>
# <li class="item_acttve"><a href=link3.html">Third item</a></li>
# <li class="item_0"><a href=link4.html">Fourth item</a></li>
# <li class="item_1"><a href=link5.html">Five item</a></li>
# </ul>
# </div>
# """

# html = etree.HTML(text)
# result = html.xpath('//li[@class="item_0"]')
# # result1=html.xpath("//ul/li/..")
# print(type(result))
# print(result)
# # print(type(result1))
# # print(result1)
