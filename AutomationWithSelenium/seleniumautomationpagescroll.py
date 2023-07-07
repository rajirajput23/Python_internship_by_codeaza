from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


s=Service("C:/Users/ZOHAIB/Documents/selenium p/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.google.com/search?sxsrf=AB5stBgkmI9YTIwsA1QXqOkLYCcZ9dM26g:1688649721024&q=Photos+of+pandas&uds=GyUA-OUbyzEsGcvQN6-SichRSCEoDwjBF2SE37_gRme8w3HplAI&tbm=isch&sa=X&ved=2ahUKEwig05W2lvr_AhWoU6QEHcnEASgQ0pQJegQIFBAB&biw=1517&bih=772&dpr=0.9")
height=driver.execute_script("return document.body.scrollHeight")
print(height)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")