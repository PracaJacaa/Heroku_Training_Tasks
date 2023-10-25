from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/abtest")
element = driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a')

current_window_handle = driver.current_window_handle

element.click()

current_url = driver.current_url
print("First page: " + current_url)

for window_handle in driver.window_handles:
    if window_handle != current_window_handle:
        driver.switch_to.window(window_handle)
        break

new_url = driver.current_url
print("New URL: " + new_url)

driver.quit()