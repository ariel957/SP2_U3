from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.anses.gob.ar/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mapa-de-sitio"]/a').click()
time.sleep(2)