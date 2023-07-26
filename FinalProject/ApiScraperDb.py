from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import mysql.connector as conn

from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!' 


#options=Options()
#driver=webdriver.Chrome(options=Options)

s=Service("C:/Users/ZOHAIB/Documents/selenium p/chromedriver.exe")
driver=webdriver.Chrome(service=s)

@app.route('/')
def main():
    driver.get('https://finance.yahoo.com/lookup?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAALIPlnt5ZBug91VITlGcJKmOCADZa4vcRX-PjGzik-l1UZ38sVGNa2MDau5EJVUmOynefeGsvQuyyCLsybl2OIB0D90uZ1Y-nsz0A7AGLb1Q_5bTrku7Y6AtANIb2bfpk5WzT3zNcAp0cw8majtLW90exhvChzEZ6RqCGkbBt0tK')
    
    tablebody=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/section/section/div/div/div/table/tbody')
    global data
    data=[]

    for tr in tablebody.find_elements(By.XPATH,'//tr'):
        row=[item.text for item in tr.find_elements(By.XPATH,'//td')]
    
        data.append(row)
    print(row)

    #print(data)




if __name__=='__main__':
    main()
    app.run(debug=True)


#creating a db connection 
mysqldb=conn.connect(host="localhost", user="root", password="zohaib@11332939", database=" ")
print(mysqldb,"done")

#Preparing a cursor object using cursor() Method
mysqlcursor=mysqldb.cursor()

#creating database

#mysqlcursor.execute('CREATE DATABASE SCRAPEDDATA')

#creating table as per requirements


mysqlcursor.execute ('create table TrendingTickers(SYMBOL VARCHAR(30),NAME VARCHAR(30), LASTPRICE VARCHAR(10), CHANGE VARCHAR(10), % CHANGE VARCHAR(10))');

"""
sql= CREATE TABLE TRENDINGTICKERS  (
SYMBOL CHAR(30),
NAME CHAR(30),
LAST PRICE CHAR,
CHANGE CHAR,
% CHANGE CHAR,
)   


mysqlcursor.execute(sql)

"""

mysqlcursor_insert_query= """  INSERT INTO TRENDING TICKERS (SYMBOL, NAME, LAST PRICE,
               CHANGE PRICE, % CHANGE) VALUES(%s, %s, %s, %s ,%s) """

records_to_insert=data
mysqlcursor.executemany(mysqlcursor_insert_query, records_to_insert)
mysqldb.commit()

print(mysqlcursor.rowcount, "Records inserted successfully into the table")

#close db connection
mysqldb.close()
