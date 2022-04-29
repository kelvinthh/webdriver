from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com.hk")

searchBar = driver.find_element_by_class_name("gLFyf.gsfi")
button = driver.find_element_by_class_name("gNO89b")

searchBar.send_keys('Hello World')
button.click()