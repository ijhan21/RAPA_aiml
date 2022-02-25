from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time  

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 
# options.add_argument("headless")  # 크롬 창을 안뜨게함.
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver_path = './chromedriver_linux64/chromedriver'
chrome = webdriver.Chrome(driver_path, options=options)
wait = WebDriverWait(chrome, 10) 
short_wait = WebDriverWait(chrome, 3) 

chrome.get("https://carbonated-cover-25d.notion.site/Web-Crawling-7b03b1ef307b43c1af0d2f4956f58345")
edit_Text="Web-Crawling"
time.sleep(10)
items = chrome.find_elements_by_css_selector('div[data-content-editable-leaf=true')
time.sleep(10)
print(items)
for item in items:
    time.sleep(3)
    item.click()
time.sleep(10)
