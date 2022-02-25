from bs4 import BeautifulSoup as BS
import requests as req

class Values:
    def __init__(self,get_list):        
        검색비율, 현재가, 전일비, 등락률, 거래량, 시가, 고가, 저가, PER,ROE = get_list
        self.검색비율=검색비율.text.strip()
        self.현재가=현재가.text.strip()
        self.전일비=전일비.text.strip()
        self.등락률=등락률.text.strip()
        self.거래량=거래량.text.strip()
        self.시가=시가.text.strip()
        self.고가=고가.text.strip()
        self.저가=저가.text.strip()
        self.PER=PER.text.strip()
        self.ROE=ROE.text.strip()
    def show(self):
        print(f"검색비율: {self.검색비율}, 현재가: {self.현재가}, 전일비: {self.전일비}, 등락률: {self.등락률}, 거래량: {self.거래량}, 시가: {self.시가}, 고가: {self.고가}, 저가: {self.저가}, PER: {self.PER},ROE: {self.ROE}", end="\n")
                

url = "https://finance.naver.com/sise/lastsearch2.nhn"
res = req.get(url)
soup = BS(res.text, "html.parser")

numbers = soup.find_all("td","number")
names = soup.find_all("a","tltle")
output=dict()
for i in range(len(names)):
    output[names[i].text]=Values(numbers[10*i:10*(1+i)])

for k, v in output.items():
    print(k,end="  ")
    v.show()


