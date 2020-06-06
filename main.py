
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
import json
import time


headless = True
linux_executable_path = './geckodriver'
win_executable_path = './geckodriver.exe'

options = Options()
options.headless = headless
driver = webdriver.Firefox(options = options , executable_path=win_executable_path)

print("please enter the URL address")
url=input()
driver.implicitly_wait(30)
driver.get("https://www.baidu.com")
driver.save_full_page_screenshot("test.png")
