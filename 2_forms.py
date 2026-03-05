import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.get("https://aqa-proka4.org/sandbox/web#forms")
    yield driver
    driver.quit()

#Валидные значения
def test_valid_values(driver):
    driver.find_element("id", "val-username").send_keys("Stanislaw")
    driver.find_element("id", "val-email").send_keys("oprishko.stas@gmail.com")
    driver.find_element("id", "val-password").send_keys("Rein223311!!!")
    driver.find_element("id", "val-confirm-password").send_keys("Rein223311!!!")
    driver.find_element("id", "valSubmitBtn").click()
    time.sleep(2)


# Невалидный логин
def test_invalid_login(driver):
    driver.find_element("id", "val-username").send_keys("Tul")
    driver.find_element("id", "val-email").send_keys("oprishko.stas@gmail.com")
    driver.find_element("id", "val-password").send_keys("Rein223311!!!")
    driver.find_element("id", "val-confirm-password").send_keys("Rein223311!!!")
    driver.find_element("id", "valSubmitBtn").click()
    time.sleep(2)
    assert "error" in driver.find_element("id", "username-error").text

# Невалидная почта
def test_invalid_email(driver):
    driver.find_element("id", "val-username").send_keys("Stanislaw")
    driver.find_element("id", "val-email").send_keys("oprishko.stas.gmail.com")
    driver.find_element("id", "val-password").send_keys("Rein223311!!!")
    driver.find_element("id", "val-confirm-password").send_keys("Rein223311!!!")
    driver.find_element("id", "valSubmitBtn").click()
    time.sleep(2)
    assert "error" in driver.find_element("id", "email-error").text

# Невалидный пароль (4 символа)
def test_invalid_password_four_symbols(driver):
    driver.find_element("id", "val-username").send_keys("Stanislaw")
    driver.find_element("id", "val-email").send_keys("oprishko.stas@gmail.com")
    driver.find_element("id", "val-password").send_keys("r123")
    driver.find_element("id", "val-confirm-password").send_keys("r123")
    driver.find_element("id", "valSubmitBtn").click()
    time.sleep(2)
    assert "error" in driver.find_element("id", "password-error").text

# Невалидный пароль (только буквы)
def test_invalid_password_only_letters(driver):
    driver.find_element("id", "val-username").send_keys("Stanislaw")
    driver.find_element("id", "val-email").send_keys("oprishko.stas@gmail.com")
    driver.find_element("id", "val-password").send_keys("rgdfhrgrgrgrgrg")
    driver.find_element("id", "val-confirm-password").send_keys("rgdfhrgrgrgrgrg")
    driver.find_element("id", "valSubmitBtn").click()
    time.sleep(2)
    assert "error" in driver.find_element("id", "password-error").text

# Невалидный пароль (только числа)
def test_invalid_password_only_numbers(driver):
    driver.find_element("id", "val-username").send_keys("Stanislaw")
    driver.find_element("id", "val-email").send_keys("oprishko.stas@gmail.com")
    driver.find_element("id", "val-password").send_keys("12345678")
    driver.find_element("id", "val-confirm-password").send_keys("12345678")
    driver.find_element("id", "valSubmitBtn").click()
    time.sleep(2)
    assert "error" in driver.find_element("id", "password-error").text

# Пароли не совпадают
def test_invalid_two_password(driver):
    driver.find_element("id", "val-username").send_keys("Stanislaw")
    driver.find_element("id", "val-email").send_keys("oprishko.stas@gmail.com")
    driver.find_element("id", "val-password").send_keys("12345678")
    driver.find_element("id", "val-confirm-password").send_keys("1234567")
    driver.find_element("id", "valSubmitBtn").click()
    time.sleep(2)
    assert "error" in driver.find_element("id", "password-error").text
       