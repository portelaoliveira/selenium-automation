from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.python.org/")

search = driver.find_element(By.ID, "id-search-field")
search.send_keys("pandas")

sleep(5)
