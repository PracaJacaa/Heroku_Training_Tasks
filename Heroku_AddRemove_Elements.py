def Length(elements):
    return len(elements)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

element = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

for i in range(100):
    element.click()

added_elements = driver.find_elements(By.CLASS_NAME, 'added-manually')

if Length(added_elements) > 0:
    print("The item has been added.")
    print("Number of elements: "+ str(Length(added_elements)))
else:
    print("The item has not been added.")


elements_to_remove = driver.find_elements(By.CLASS_NAME, 'added-manually')
for element in elements_to_remove:
    driver.execute_script("arguments[0].remove();", element)

added_elements_afterRemv = driver.find_elements(By.CLASS_NAME, 'added-manually')

if Length(added_elements_afterRemv) > 0:
    print("We failed, Number of elements left: "+ str(Length(added_elements_afterRemv)))
else:
    print("WE DID IT")

driver.quit()