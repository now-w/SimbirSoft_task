import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "none"
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()