"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


@pytest.fixture(scope = "function",
                params = [(1920, 1080), (360, 800)])
def setup_browser(request):
    browser.config.window_width, browser.config.window_height = request.param
    yield
    browser.quit()


@pytest.mark.parametrize('setup_browser', [(1920, 1080)], indirect=True, ids = lambda res: f'{res[0]}x{res[1]}')
def test_github_desktop(setup_browser):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-up').click()


@pytest.mark.parametrize('setup_browser', [(360, 800)], indirect=True, ids = lambda res: f'{res[0]}x{res[1]}')
def test_github_mobile(setup_browser):
    browser.open('https://github.com')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()


