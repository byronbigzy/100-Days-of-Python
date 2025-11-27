from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pprint import pprint

#Keep brower open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
URL = "https://www.python.org/"
driver.get(url=URL)

events = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul").find_elements(By.TAG_NAME, value="li")

event_dict = {}

for index, event in enumerate(events):
    date = event.find_element(By.TAG_NAME, value="time").get_attribute("datetime").split("T")[0]
    name = event.find_element(By.TAG_NAME, value="a").text

    event_data = {
        "date":date,
        "name":name
    }
    event_dict[index] = event_data

pprint(event_dict)

driver.quit()