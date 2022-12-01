import pytest
from selene.support.shared import browser
from selene import be, have
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def config_driver():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return browser.config.driver


@pytest.fixture()
def config_browser_size():
    browser.driver.set_window_size(700, 600)


@pytest.fixture()
def open_browser(config_driver, config_browser_size):
    browser.open('https://google.com')
