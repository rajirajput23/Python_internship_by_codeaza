from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import time

options=Options()
driver=webdriver.Chrome(options=options)
driver.get("https://tutorialsninja.com/demo/")
time.sleep(2)
driver.maximize_window()
time.sleep(8)
#driver.find_element(By.NAME,"search").send_keys("iphone")
#driver.find_element("name","search").click()
element=driver.find_element("name","search")
element.send_keys("iphone")
time.sleep(2)
print(element)
