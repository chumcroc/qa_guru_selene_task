import pytest
from selene.support.shared import browser
from selene import be, have


def test_google_search_true(open_browser):
    pos_search_in = 'selene'
    pos_search_out = 'yashaka/selene: User-oriented Web UI browser tests in Python'
    browser.element('[name="q"]').should(be.blank).type(pos_search_in).press_enter()
    browser.element('[id="search"]').should(have.text(pos_search_out))


def test_google_search_false(open_browser):
    neg_search = 'ajdasjadsjkdsakld dsaldjsald ld alda jsakd'
    neg_search_result = f'Your search - {neg_search} - did not match any documents.'
    browser.element('[name="q"]').should(be.blank).type(neg_search).press_enter()
    browser.element('[id="rcnt"]').should(have.text(neg_search_result))
