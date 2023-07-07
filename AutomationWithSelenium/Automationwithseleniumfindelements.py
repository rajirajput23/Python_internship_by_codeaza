from selenium import webdriver
from selenium.webdriver.chrome.options import Options   
#from selenium.webdriver.chrome.options import Service
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options=Options()

driver=webdriver.Chrome(options=options)
time.sleep(2)
driver.get("https://meet.google.com/ecm-okyf-ofm?hs=224")
#driver.find_element_by_xpath ("""/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span""").click()

time.sleep(10)


driver.find_element("xpath","""//*[@id="yDmH0d"]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span""").click()

driver.quit()