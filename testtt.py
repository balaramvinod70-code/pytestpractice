from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Edge()
driver.get("https://www.amazon.com")
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search.send_keys("Oneplus")
search.send_keys(Keys.ENTER)
action = ActionChains(driver)
for i in range(10):
    action.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
for i in range(10):
    action.send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)
driver.quit()

