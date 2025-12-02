from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pprint import pprint
import time

#Keep brower open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
URL = "https://ozh.github.io/cookieclicker/"
driver.get(url=URL)

# Potato Ah PC can't load website fast enough
time.sleep(5)
driver.find_element(By.ID, value="langSelect-EN").click()

time.sleep(3)
cookie = driver.find_element(By.ID, value="bigCookie")

while True:

    available_upgrades = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")

    if available_upgrades:
        most_expensive = available_upgrades[-1]
        most_expensive.click()
    else:
        cookie.click()

driver.quit()