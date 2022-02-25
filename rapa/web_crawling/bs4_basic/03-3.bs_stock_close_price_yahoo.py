from bs4 import BeautifulSoup as BS
import requests as req

COUNT = 25
offset=0
with open('output.csv', 'w') as f:
    cols = "names, prices, changes, volumes\n"
    f.writelines(cols)
while True:
    url = f"https://finance.yahoo.com/most-active?count{COUNT}=&offset={offset}&count={COUNT}"
    res = req.get(url)
    soup = BS(res.text, "html.parser")
    names= soup.find_all('td',{'aria-label':'Name'})
    prices = soup.find_all('td',{'aria-label':'Price (Intraday)'})
    changes = soup.find_all('td',{'aria-label':'Change'})
    volumes = soup.find_all('td',{'aria-label':'Volume'})
    with open('output.csv', 'a') as f:
        for i in range(len(names)):
            data=""
            data += names[i].text.split()[0]+','
            data += prices[i].text.split()[0]+','
            data += changes[i].text.split()[0]+','
            data += volumes[i].text.split()[0]+'\n'
            f.writelines(data)        
    offset+=COUNT
    if offset>=224:
        break
