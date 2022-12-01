import pytest
from selene.support.shared import browser
from selene import be, have


def test_google_search_true(open_browser):
    """Вводим переменные pos_search_in в кач-ве строки ввода и pos_search_in к кач-ве искомой строки"""

    pos_search_in = 'selene'
    pos_search_out = 'yashaka/selene: User-oriented Web UI browser tests in Python'

    """С помощью selenium при запуске браузера в поисковике ищется переменная pos_search_in,
    после исполняется вторая строка кода, кот-я ищет на страницу переменную pos_search_out"""

    browser.element('[name="q"]').should(be.blank).type(pos_search_in).press_enter()
    browser.element('[id="search"]').should(have.text(pos_search_out))


def test_google_search_false():
    """Вводим переменную neg_search со значением 'dsadsadadsadx'"""

    neg_search = 'dsadsadadsadx'
    neg_search_result = f'Результатов с именем "{neg_search}" не найдено'

    """ """

    browser.element('name="q"').should(be.blank).type(neg_search).press_enter()
    browser.element('[class="gLFyf"]').should(have.text(neg_search_result))
