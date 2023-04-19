from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import time

from main import ya_password, email


def authentication():
    url = 'https://passport.yandex.ru/auth/'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(1)

    login = driver.find_element(By.ID, "passp-field-login")
    time.sleep(1)
    login.click()
    time.sleep(1)
    login.send_keys(email)
    time.sleep(1)

    enter_btn = driver.find_element(By.ID, 'passp:sign-in')
    time.sleep(1)
    enter_btn.click()
    time.sleep(1)

    password = driver.find_element(By.NAME, 'passwd')

    time.sleep(1)
    password.click()
    time.sleep(1)
    password.send_keys(ya_password)
    time.sleep(1)

    log_btn = driver.find_element(By.ID, 'passp:sign-in')
    time.sleep(1)
    log_btn.click()

    time.sleep(1)
    main_url = driver.current_url

    driver.close()
    driver.quit()
    return main_url


class TestAuth(unittest.TestCase):
    def test_login(self):
        expected = 'https://id.yandex.ru/'
        result = authentication()
        self.assertEqual(expected, result)