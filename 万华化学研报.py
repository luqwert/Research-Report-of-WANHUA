#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
# @Author  : lusheng

from bs4 import BeautifulSoup
import urllib.request
import re

# 万华研报列表地址
urlbase = 'http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/search/index.phtml?t1=2&symbol=600309&p='
f = open('test.txt', 'w', encoding='utf-8')
for i in range(1, 4):
    url = urlbase + str(i)
    print('从第%d页下载研报清单' % i)
# 下载网页
    req = urllib.request.Request(url)
    response1=urllib.request.urlopen(req)
    html=response1.read().decode('gbk')
    # print(html)


    #分析网页数据、获取研报地址
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.prettify())
    lists = soup.find_all('td', class_="tal f14")
    # print(list)
    links = []
    for tag in lists:
        link = tag.find('a').get('href')
        title = tag.find('a').get('title')
        # 链接全部存储在links列表中
        links.append(link)
        print(link, title)

# 下载研报网页内容


    print(len(links))
    for link1 in links:
        print(link1)
        req3 = urllib.request.Request(link1)
        response3 = urllib.request.urlopen(req3)
        html3 = response3.read().decode('gbk','ignore')
        # print(html3)
        soup3 = BeautifulSoup(html3, "html.parser")
        # print(soup3)
        ptitle = soup3.find_all('h1')
        pcontent = soup3.find_all('p')
        ptitle2 = str(ptitle)
        pcontent2 = str(pcontent)
        print(ptitle2,pcontent2)
        f.write(ptitle2)
        f.write('\n')
        f.write(pcontent2)
        f.write('\n\n')
# 建立txt文件

f.close()

# for rur2 in links:
#     req2 = urllib.request.Request(rur2)
#     response2 = urllib.request.urlopen(req)
#     html2 = response2.read().decode('gbk')
#     # print(html2)
#     soup2 = BeautifulSoup(html2, "html.parser")
#     ptitle = soup2.find_all('div', class_="content")
#     pcontent = soup2.find('div', class_="blk_container")
#     # content = pcontent.find('p').get('content')
#     print(ptitle,pcontent)
    # for tag in lists2:
    #     content = tag.find('a').get('content')
    #     title2 = tag.find('a').get('title')
    #     print(title2,content)
# 分析网页数据，获取研报内容

# 存储研报文件


