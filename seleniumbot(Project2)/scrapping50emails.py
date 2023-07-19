import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
import time


# Set up Selenium WebDriver
options=Options()
driver= webdriver.Chrome(options=Options)

#driver= webdriver.Chrome('C:/Users/ZOHAIB/Documents/selenium p/chromedriver.exe') 

website_url = 'https://www.randomlists.com/email-addresses?qty=50'  #  the actual group URL
driver.get(website_url)

page_Source=driver.page_source

EMAIL_REGEX=r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

list_of_emails=[]

for re_match in re.finditer(EMAIL_REGEX,page_Source):
    list_of_emails.append(re.match.group())

for i, email in enumerate(list_of_emails):
    print(f'{i+1}:{email}')

driver.close()