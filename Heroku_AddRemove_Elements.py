#Here is a funcion that counts how many elements there are
def Length(elements):
    return len(elements)

#Importing nessesery module and class 
from selenium import webdriver
from selenium.webdriver.common.by import By

#Our target and new object 
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

#We find element to test
element = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

#Loop to add 100 new elements
for i in range(100):
    element.click()

added_elements = driver.find_elements(By.CLASS_NAME, 'added-manually')

if Length(added_elements) > 0:
    print("The item has been added.")
    print("Number of elements: "+ str(Length(added_elements)))
else:
    print("The item has not been added.")

#Clicking 100 times on new element to remove it
for z in range(100):
    added_elements = driver.find_element(By.CLASS_NAME, 'added-manually')
    added_elements.click()

# Here is a method to remove all elements with use of JavaScript script#
#elements_to_remove = driver.find_elements(By.CLASS_NAME, 'added-manually')
#for element in elements_to_remove:
#    driver.execute_script("arguments[0].remove();", element)

added_elements_afterRemv = driver.find_elements(By.CLASS_NAME, 'added-manually')

if Length(added_elements_afterRemv) > 0:
    print("We failed, Number of elements left: "+ str(Length(added_elements_afterRemv)))
else:
    print("WE DID IT")

driver.quit()