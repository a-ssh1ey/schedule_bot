import time
from array import *
import os
os.chmod('C:/Users/38066/PycharmProjects/parsing/chromedriver', 800)
import fake_useragent
import requests, requests.utils, pickle
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
link = "http://liceyn1.pl.ua/Account/LogOn?ReturnUrl=/"
link_shedule = ["http://liceyn1.pl.ua/Education/Diary?schoolId=2&targetProfileId=3024&groupId=153",
"http://liceyn1.pl.ua/Education/Diary?schoolId=2&targetProfileId=3012&groupId=153"]
user = fake_useragent.UserAgent().random
session = requests.Session()
options = webdriver.ChromeOptions()
options.add_argument(user)
driver = webdriver.Chrome(executable_path=r"C:\Users\38066\PycharmProjects\parsing\chromedriver\chromedriver.exe")
header ={
    'user-agent': user
}
Emails = ["soboleva-an@daypad.com.ua","loboda-ig@daypad.com.ua"]
Passwords = ["123456","123456"]
shedules = [ [ [],[],[],[],[],[] ], [ [],[],[],[],[],[] ] ]
for e in range(0,2):
    try:
        driver.get(url=link_shedule[e])
        time.sleep(2)
        email_input = driver.find_element_by_id("Email")
        email_input.clear()
        email_input.send_keys(Emails[e])
        time.sleep(2)
        password_input = driver.find_element_by_id("Password")
        password_input.clear()
        password_input.send_keys(Passwords[e])
        time.sleep(2)
        button = driver.find_element_by_id("sign-in").click()
        time.sleep(3)
        html = driver.page_source
        #print(html)
        for j in range(1, 7):
            h = driver.find_element_by_xpath(f'//*[@id="diary"]/h4[{j}]')
            shedules[e][j-1].append(h.text)
            for i in range (1, 8):
                try:
                    sh = driver.find_element_by_xpath(f'//*[@id="diary"]/table[{j}]/tbody/tr[{i*2-1}]/td[2]/a')
                    shedules[e][j-1].append(sh.text)

                except:
                    pass
    #//*[@id="diary"]/table[1]/tbody/tr[1]/td[2]/a
    #//*[@id="diary"]/table[1]/tbody/tr[3]/td[2]/a
    #//*[@id="diary"]/table[1]/tbody/tr[5]/td[2]/a
    #//*[@id="diary"]/table[2]/tbody/tr[1]/td[2]/a
        exit = driver.find_element_by_xpath("/ html / body / div[1] / div / ul[2] / li / a").click()
    except Exception as ex:
        print(ex)

driver.close()
#//*[@id="diary"]/h4[2]
print(shedules)
print(shedules[0][0])
print(shedules[0][0][7])
print(len(shedules[0][0]))
