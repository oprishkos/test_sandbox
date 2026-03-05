import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge()
driver.get("https://aqa-proka4.org/sandbox/")

# url = driver.current_url
# print("Url страницы: ", url)
# assert url == "https://aqa-proka4.org/sandbox/", "Url страницы не соответствует ожидаемому"

# title = driver.title
# print("Title страницы: ", title)

print(driver.page_source) # Выводим исходный код страницы


time.sleep(2)



