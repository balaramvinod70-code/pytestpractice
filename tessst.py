from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base64
driver = webdriver.Chrome()
driver.get("https://varadharajatheatres.com/")
driver.maximize_window()
s=driver.find_element(By.TAG_NAME,"body")
s=ActionChains(driver)
for i in range(2):
    s.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1)
    s.send_keys(Keys.PAGE_UP).perform()
    time.sleep(1)
result=driver.execute_cdp_cmd("Page.captureScreenshot",{"captureBeyondViewport":True})
with open("vara.png","wb") as f:
    f.write(base64.b64decode(result['data']))
    print(8)
time.sleep(5)
driver.close()
