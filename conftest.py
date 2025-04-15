import pytest
from selene import browser


@pytest.fixture
def driver():
    browser.config.window_width = 1920
    browser.config.window_heigh = 1080
    browser.open('https://ya.ru/')

    yield browser

    browser.quit()