from bs4 import BeautifulSoup as BS
import requests as req
import numpy as np

page = 1
title_list = list()
rate_list = list()
while True:
    url = "https://comic.naver.com/webtoon/list?titleId=335885&page="+str(page)
    res = req.get(url)
    soup = BS(res.text, "html.parser")
    titles = soup.find_all("td","title")
    title_list += [title.text.strip() for title in titles]
    rates = soup.find_all("div","rating_type")
    rate_list += [float(rate.text.split()[1]) for rate in rates]
    page+=1
    if title_list[-1][:2]=='1화':
        break
output = {'titles':title_list, 'rates':rate_list}

print(output)
print("전체점수 : ",np.sum(rate_list))
print("평균점수 : ",np.mean(rate_list))