from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

path = os.getcwd()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("prefs", {
  "download.default_directory": path + r"\test",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://www.bimobject.com/pt-br")
sleep(5)

conection = driver.find_element(By.ID, "navbar-button-signin")
conection.click()
sleep(5)

google = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/div[2]/button[1]")
google.click()
sleep(2)

login = driver.find_element(By.ID, "identifierId")
login.clear()
login.send_keys("abigail.ramos@ruraltech.com.br")
next_ = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
next_.click()
sleep(2)
password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password.clear()
password.send_keys("Biga209*")
login_click = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
login_click.click()
sleep(10)

software = driver.find_element(By.CLASS_NAME, "button-content")
software.click()
revit_item = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-nav/div[2]/div/form/app-search-input/div/div[1]/div/app-search-bar-filter/div/app-software-filter/div/div/ul/li[1]")
revit_item.click()
sleep(1)

search = driver.find_element(By.NAME, "search")
search.send_keys("parede")
sleep(1)
search_button = driver.find_element(By.CLASS_NAME, "text")
search_button.click()
sleep(2)

# print([my_href.get_attribute("href") for my_href in WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.product-card-title")))])
# link = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-search-page/div/div[2]/div[2]/app-search-results/div/div/app-product-card[4]/div/div[1]/div[2]/a[2]").get_attribute('href')
# print(link)

link = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-search-page/div/div[2]/div[2]/app-search-results/div/div/app-product-card[4]/div/div[1]/div[2]/a[2]")
link.click()
sleep(4)

download_link = driver.find_element(By.CLASS_NAME, "download-button-text")
download_link.click()
sleep(2)

deselect = driver.find_element(By.NAME, "checkbox")
deselect.click()
sleep(1)

select_revit = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-product-page/app-neu-download-modal/div[1]/div/div/div[3]/ul/li/div/div/div[1]/span[1]")
if select_revit.text == "Revit":
    select_revit.click()
sleep(2)

download_file = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-product-page/app-neu-download-modal/div[1]/div/div/div[4]/button[1]/span")
download_file.click()
sleep(2)

close = driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-product-page/app-neu-download-modal/div[1]/div/app-download-modal-recommendations/div/div[2]/button")
close.click()

sleep(20)
