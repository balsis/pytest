"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser


@pytest.fixture(scope = "function", params = [(1920, 1080), (1366, 768), (1536, 864)],
                ids = lambda res: f'{res[0]}x{res[1]}')
def desktop_browser(request):
    browser.config.window_width, browser.config.window_height = request.param
    yield
    browser.quit()


@pytest.fixture(scope = "function", params = [(360, 800), (390, 873), (390, 844)],
                ids = lambda res: f'{res[0]}x{res[1]}')
def mobile_browser(request):
    browser.config.window_width, browser.config.window_height = request.param
    yield
    browser.quit()


def test_github_desktop(desktop_browser):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-up').click()


def test_github_mobile(mobile_browser):
    browser.open('https://github.com')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
