from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

requirement = ["ROPA DE CAMA\nBAÑO\nCOCINA\nDECORACIÓN\nDISNEY\nNAVIDAD\nCONOCENOS"]

def compareLabels():
    if requirement == list_elements:
        print("Pass")
    else:
        print("Fail")


website = "https://www.arredo.com.ar/"
driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()
time.sleep(2)
action = ActionChains(driver)
time.sleep(2)

action.move_to_elemnt(driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul'))
action.perform()
time.sleep(2)
list_elements =[]
#extraemos los textos del contenedor para validar nombres y los guardamos en una lista
element = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul').text
list_elements.append(element)
#implementamos la funcion
compareLabels()
time.sleep(2)
print(list_elements)
print(requirement)
print("programa finalizado")
driver.close()
