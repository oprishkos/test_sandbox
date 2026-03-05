import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge()
driver.get("https://aqa-proka4.org/sandbox/web#forms")

driver.find_element("id", "username").send_keys("Stanislaw")
driver.find_element("id", "email").send_keys("stanislaw@gmail.com")
driver.find_element("id", "password").send_keys("1234567890")
country =driver.find_element("id", "country")
select = Select(country)
select.select_by_visible_text("Russia")
driver.find_element("id", "terms").click()
driver.find_element("id", "submitBtn").click()

time.sleep(2)

assert "успешно" in driver.find_element("id", "formResult").text


