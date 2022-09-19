from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class BlackBoard:

    def __init__(self):
        self.jobs = []
        self.jobs_link = []
        self.selenium_service = Service("D:/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.selenium_service)
        self.driver.get("https://justjoin.it/all/python/junior")
        self.elements = self.driver.find_elements(By.CSS_SELECTOR, "div.jss234")
        self.links = self.driver.find_elements(By.TAG_NAME, "a")

    time.sleep(5)  # To let page load properly

    def job_search(self):
        for element in self.elements:
            self.jobs.append(element.text)

        for link in self.links:
            self.jobs_link.append(link.get_attribute("href"))
        self.jobs = [i.split('\n',1)[0] for i in self.jobs]
        self.jobs_link = self.jobs_link[8:]
        print(self.jobs)
        print(self.jobs_link)


test = BlackBoard()
test.job_search()

