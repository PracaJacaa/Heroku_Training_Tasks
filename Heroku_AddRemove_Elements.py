from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

element = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

for i in range(100):
    element.click()

for z in range(100):
    Del_element = driver.find_element(By.CLASS_NAME, 'added-manually')
    Del_element.click()

driver.quit()