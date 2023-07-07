from selenium import webdriver
from selenium.webdriver.chrome.options import Options   
#from selenium.webdriver.chrome.options import Service
import os
import time
from selenium.webdriver.common.by import By

options=Options()

driver=webdriver.Chrome(options=options)
driver.get("")
time.sleep(10)
#driver.find_element_by_xpath ("""/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span""").click()

driver.find_element(By.XPATH,"""/html/body/div[8]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[1]/div/span/span/table/tbody/tr/td/table[2]/tbody/tr/td/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/a/table/tbody/tr/td/span""").click()

driver.quit()


