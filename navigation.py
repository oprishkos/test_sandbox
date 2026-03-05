import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge()

driver.get("https://aqa-proka4.org/sandbox/")
time.sleep(3)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()

time.sleep(3)