from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
j=webdriver.Edge()
j.get("https://www.amazon.com")
j.maximize_window()
s=WebDriverWait(j,10).until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox")))
s.send_keys("Nothing 3a")
s.send_keys(Keys.ENTER)
d=ActionChains(j)
for i in range(9):
    d.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
for i in range(9):
    d.send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)
j.minimize_window()
time.sleep(6)
j.close()
