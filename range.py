import requests
from bs4 import BeautifulSoup
import os
# FTC的赛季排名资料
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}
tag = 1701
count = 0
# os.mkdir('2018赛季FTC队伍名单')
while (tag<1745):
    html = requests.get('http://www.firstchina.org.cn/FTC/FTCNews.aspx?id='+str(tag), UA).content
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)
    print('============================================')
    sweet_soup = soup.find('table')
    lovely_soup = soup.find('h1')
    if (sweet_soup!=None):
        # print(sweet_soup)
        title = lovely_soup.getText()
        titles = ''.join(title.split())
        print(titles)
        info = sweet_soup.getText()
        f = open(str(titles)+'.txt','w',encoding='utf-8')
        f.write(str(title)+"\n"+str(info))
        f.close()
        print(info)
        print("-----------------------------------------"+str(tag)+"-------------------------------------------------------------")
        tag = tag+1
        count = count + 1
    else:
        print("-----------------------------------------" + str(tag) + "-------------------------------------------------------------")
        tag = tag + 1
        continue
print('=============finish===============')