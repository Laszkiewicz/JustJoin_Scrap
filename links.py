from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("D:/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://justjoin.it/all/python/junior")
time.sleep(5)
links = driver.find_elements(By.TAG_NAME, "a")
print(links)


for link in links:
    print(link.get_attribute("href"))


driver.quit()