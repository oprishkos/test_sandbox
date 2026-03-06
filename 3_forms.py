import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.get("https://aqa-proka4.org/sandbox/web#forms")
    yield driver
    driver.quit()

# Валидные значения
def test_multiple_emails_phones(driver):
    driver.find_element("id", "dyn-name").send_keys("Stanislaw")
    time.sleep(2)
    # Обработка с email
    driver.find_element(By.CSS_SELECTOR, "#emailFields input").send_keys("stas1@gmail.com")
    time.sleep(2)
    driver.find_element("id", "addEmailBtn").click()
    time.sleep(2)
    emails = driver.find_elements(By.CSS_SELECTOR, "#emailFields input")
    time.sleep(2)
    emails[-1].send_keys("second@example.com")
    time.sleep(2)

    # Обработка с phone
    driver.find_element(By.CSS_SELECTOR, "#phoneFields input").send_keys("+766612345")
    time.sleep(2)
    driver.find_element("id", "addPhoneBtn").click()
    time.sleep(2)
    phones = driver.find_elements(By.CSS_SELECTOR, "#phoneFields input")
    time.sleep(2)
    phones[-1].send_keys("+76544444")
    time.sleep(2)
    driver.find_element("id", "dynSubmitBtn").click()
    time.sleep(2)

def test_delete_emails_phones(driver):
    driver.find_element("id", "dyn-name").send_keys("Stanislaw")
    time.sleep(2)
    # Обработка с email
    driver.find_element(By.CSS_SELECTOR, "#emailFields input").send_keys("stas1@gmail.com")
    time.sleep(2)
    driver.find_element("id", "addEmailBtn").click()
    time.sleep(2)
    emails = driver.find_elements(By.CSS_SELECTOR, "#emailFields input")
    time.sleep(2)
    emails[-1].send_keys("second@example.com")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#emailFields button").click() # Удаление email
    time.sleep(2)

    # Обработка с phone
    driver.find_element(By.CSS_SELECTOR, "#phoneFields input").send_keys("+766612345")
    time.sleep(2)
    driver.find_element("id", "addPhoneBtn").click()
    time.sleep(2)
    phones = driver.find_elements(By.CSS_SELECTOR, "#phoneFields input")
    time.sleep(2)
    phones[-1].send_keys("+76544444")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#phoneFields button").click()
    time.sleep(2)
    driver.find_element("id", "dynSubmitBtn").click()
    time.sleep(2)

