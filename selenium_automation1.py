from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
driver.get("https://demoqa.com/text-box")

print(driver.title)

import time
time.sleep(5)
driver.quit()
