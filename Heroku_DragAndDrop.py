from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

FailExit = 0
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/drag_and_drop")

### Looking for column A by id
A_element = driver.find_element(By.ID, 'column-a')

try:
    A_element = driver.find_element(By.ID, 'column-a')
except NoSuchElementException:
    print("Element A not found")
    FailExit = 1

### Looking for column B by id
B_element = driver.find_element(By.ID, 'column-b')

try:
    B_element = driver.find_element(By.ID, 'column-b')
except NoSuchElementException:
    print("Element B not found")
    FailExit = FailExit +1
    if FailExit == 2:
        ### First exit fail exit criteria
        print("Both elements were not found.")
        driver.quit()

### Second exit fail exit criteria
if FailExit == 1:
        print("One element were not found.")
        driver.quit()

### Saving locations of elements before drag and drop
locationA = A_element.location
locationB = B_element.location

### Created new action chain object, to perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(A_element, B_element).perform()

### Wait for a site to drop element, as elements is swiches from column-a to column-b
### We read location of column-b
time.sleep(2)
New_locationA = B_element.location

if New_locationA == locationB:
    print("Test has been marked as Pass")
else:
     print("We failed")
driver.quit()