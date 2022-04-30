from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=/Users/kelvintam/Library/Application Support/Google/Chrome")
# options.add_argument('--profile-directory=Profile 1')
# options.page_load_strategy = 'normal'

# browser = webdriver.Chrome(chrome_options=options)
browser = webdriver.Chrome()
browser.get("https://www.google.com")

searchInput = browser.find_element(By.CLASS_NAME, "gLFyf.gsfi")
button = browser.find_element(By.CLASS_NAME, "gNO89b")
searchInput.send_keys("Half Life 3 when")
sleep(0.1)
button.click()

link = browser.find_element(By.PARTIAL_LINK_TEXT, "reportedly")
link.click()

# /Users/kelvintam/Library/Application Support/Google/Chrome/Profile 1

# browser = webdriver.Chrome(chrome_options=options)