from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Edge()
driver.get("https://www.amazon.com")
driver.maximize_window()
dropdown=Select(driver.find_element(By.XPATH,"//*[@id='searchDropdownBox']"))
dropdown.select_by_index(10)
d=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox")))
d.send_keys("iphone")
d.send_keys(Keys.RETURN)
oo=ActionChains(driver,10)
for i in range(10):
    oo.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(5)
for i in range(10):
    oo.send_keys(Keys.PAGE_UP).perform()
    time.sleep(5)
time.sleep(7)
driver.quit()
