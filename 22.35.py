from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Edge()
driver.get("https://www.google.com")
driver.maximize_window()
search=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"q")))
search.send_keys("nokia")
search.send_keys(Keys.RETURN)
action=ActionChains(driver)
for i in range(9):
    action.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
for i in range(9):
    action.send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)
driver.minimize_window()
time.sleep(5)
driver.quit()