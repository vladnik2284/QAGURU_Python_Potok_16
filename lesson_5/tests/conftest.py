import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    # from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options
    # o = Options()
    # o.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=o)
