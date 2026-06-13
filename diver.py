from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
diver=webdriver.Edge()
diver.get("https://www.amazon.com")
diver.maximize_window()
son=WebDriverWait(diver,10).until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox")))
son.send_keys("Oneplus nord 6")
son.send_keys(Keys.RETURN)
d=ActionChains(diver)
for i in range(10):
    d.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
for i in range (10):
    d.send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)
diver.minimize_window()
time.sleep(10)
diver.quit()