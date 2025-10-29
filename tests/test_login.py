from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Jenkins Selenium Python")
    search_box.submit()
    assert "Jenkins" in driver.page_source
    driver.quit()
