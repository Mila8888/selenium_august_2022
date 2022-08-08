import pytest
import os

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="browser to run tests"
    )
    parser.addoption(
        "--headless", action="store_true", help="browser to run tests"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            options.headless = True

        _driver = webdriver.Chrome(
            executable_path=os.path.expanduser("~/Downloads/drivers/chromedriver"),
            options=options
        )
    elif browser_name == "firefox":
        _driver = webdriver.Firefox(executable_path=os.path.expanduser("~/Downloads/drivers/geckodriver"))
    elif browser_name == "opera":
        _driver = webdriver.Opera(executable_path=os.path.expanduser("~/Downloads/drivers/operadriver"))
    elif browser_name == "yandex":
        _driver = webdriver.Chrome(executable_path=os.path.expanduser("~/Downloads/drivers/yandexdriver"))
    elif browser_name == "safari":
        _driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {browser_name} is not supported.")

    yield _driver

    _driver.close()
