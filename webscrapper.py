from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
from itertools import cycle
import pandas as pd
import logging
import requests
import random
import time
import os


class alina_ws_login():

    def __init__(o):
            o.url = "https://www.facebook.com/NASA/"
            o.proxyurl = "https://free-proxy-list.net/"
            o.headers = {"UserAgent":"Applebot"}
            o.rob_tex_url = "https://www.facebook.com/robots.txt"
            o.chrome_path = r"C:\Driver\chromedriver.exe"
            o.UserName = "yourmail"
            o.PassWord = "yourpassword"
            #o.headless = None
            #o.OS = None
            #o.TargetDB = None
            #o.LastAccess = datetime
            #o.LastFailure = datetime
            #o.Status = None
            #o.ScrapMethod = None


    def GetRobotTxt(o):
            
            driver = webdriver.Chrome(o.chrome_path)
            driver.get(o.rob_tex_url)
            print(driver)
            driver.close()
            return      

    def getproxiesIP(o):
            
            ip = requests.get(o.proxyurl)
            prx =  BeautifulSoup(ip.text,"html.parser")
           
            t = random.randint(4,15)
            time.sleep(t)
            print(t)

            ipadress = []
            ports = [] 

            for i in prx.find_all('td')[::8]:
                ipadress.append(i.text)
            

            for j in prx.find_all('td')[1::8]:
                ports.append(j.text)
           

            proxyset = set(zip(ipadress,ports))
                      
            return proxyset
            
            
    def FBlogin(o):
            
            proxyset =o.getproxiesIP()
            pro = cycle(proxyset)
            proxys = next(pro)
            e =   print(proxys)
            path = o.chrome_path
            driver = webdriver.Chrome(o.chrome_path)
            driver.get(proxies={"https":e})
            driver.get(o.url,headers=o.headers)
            driver.maximize_window()
            sl = random.randint(3,32)
            time.sleep(sl)

            user_id = driver.find_element_by_id('email')
            user_password = driver.find_elements_by_xpath('//*[@id="loginbutton"]')

            user_id.send_keys(o.UserName)
            user_password.send_keys(o.PassWord)
            login_button[0].click()
            
           
        


if __name__ == "__main__" :

             ob = alina_ws_login()
             ob.getproxiesIP()
             ob.FBlogin()


