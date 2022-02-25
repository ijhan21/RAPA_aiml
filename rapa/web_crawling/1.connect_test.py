from selenium import webdriver
import time

driver_path = '/home/hans/web_crawling/chromedriver_linux64/chromedriver'
chrome = webdriver.Chrome(driver_path)
chrome.get("http://naver.com")
time.sleep(3)
chrome.close()