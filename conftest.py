import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def open_browser():
    browser.config.window_width = 1000
    browser.config.window_height = 1200
    browser.open('https://google.com')
