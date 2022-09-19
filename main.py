from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("D:/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://justjoin.it/all/python/junior")
time.sleep(5)
elements = driver.find_elements(By.CSS_SELECTOR, "div.jss234")

for element in elements:
    print(element.text)

driver.quit()

# job = input("Please inform what technology or all ").lower()
# level = input("please inform what level are you junior/mid/senior  ").lower()
# contract = input("please inform what contract are you searching b2b/mandate/permanent ").lower()
#
# html = f"https://justjoin.it/all/{job}/{level}?employmentType={contract}"
#
# print(html)
# html_text = requests.get(html).text
# soup = BeautifulSoup(html_text, 'html.parser')
# posters = soup.find_all(name='a', class_='jss1763')
#
# posters_text = []
# posters_salary = []
#
# for poster in posters:
#     text = poster.get_text()
#     posters_text.append(text)
#
# print(posters_text)
# print(soup)
