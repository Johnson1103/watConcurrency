
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
chromedriver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"  # 这里是你的驱动的绝对地址
browser = webdriver.Chrome(chromedriver)

# 设置浏览器需要打开的url
url = "https://www.ixigua.com/home/800093389722574/?wid_try=1"
browser.get(url)