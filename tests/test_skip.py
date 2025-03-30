"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser


def is_mobile(resolution):
    width, height = resolution
    return width <= 1024


@pytest.fixture(scope = "function",
                params = [(1920, 1080), (360, 800)],
                ids = lambda res: f'{res[0]}x{res[1]}')
def setup_browser(request):
    width, height = request.param
    browser.config.window_width, browser.config.window_height = width, height
    yield "desktop" if width >= 900 else "mobile"
    browser.quit()


def test_github_desktop(setup_browser):
    if setup_browser == "mobile":
        pytest.skip(reason = "It is mobile resolution")
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-up').click()


def test_github_mobile(setup_browser):
    if setup_browser == "desktop":
        pytest.skip(reason = "It is desktop resolution")
    browser.open('https://github.com')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
