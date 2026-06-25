from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base64
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
l=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"username")))
l.send_keys("Admin")
s=driver.find_element(By.NAME,"password")
s.send_keys("admin123")
s.send_keys(Keys.ENTER)
o=ActionChains(driver)
for i in range(2):
    o.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
for i in range(2):
    o.send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)
RESULT=driver.execute_cdp_cmd("Page.captureScreenshot",{"captureBeyondViewport":True})
with open("kin.png","wb")as f:
    f.write (base64.b64decode(RESULT['data']))
    print("bala will try")
time.sleep(5)
driver.back()
driver.quit()
