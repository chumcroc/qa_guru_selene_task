import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def open_browser():
    browser.config.window_width = 600
    browser.config.window_height = 800
    browser.open('https://google.com')
