from selenium import webdriver
from selenium.webdriver.common.by import By
import time

requirement = "Suscribite al Newsletter"


def compareLabels():
    if requirement == labelObtained:
        print("Pass")
    else:
        print("Fail")


website = "https://www.arredo.com.ar/"
driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()
time.sleep(2)
# ingresamos a "Conocenos"
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[7]/div/a/div').click()
time.sleep(2)
# Extraemos el texto del label
subscriptionNewsletter = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[5]/div/div[2]/div[1]/div/div/div/div/form/label').text
labelObtained = subscriptionNewsletter
#implementamos la funcion
compareLabels()
time.sleep(2)
#volvemos a la HOme
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/p/a').click()
time.sleep(5)
#aceptamos Modal emergente al volver al Home
driver.find_element(By.ID, 'btnNoIdWpnPush').click()
time.sleep(5)
print("programa finalizado")
driver.close()
