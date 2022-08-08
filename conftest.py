import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="browser to run tests"
    )
    parser.addoption(
        "--drivers", default=os.path.expanduser("~/Downloads/drivers"), help="browser to run tests"
    )
    parser.addoption(
        "--headless", action="store_true", help="browser to run tests"
    )
    parser.addoption(
        "--base_url", default="http://192.168.0.101:8081/", help="browser to run tests"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drivers_folder = request.config.getoption("--drivers")
    base_url = request.config.getoption("--base_url")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=f"{drivers_folder}/chromedriver",)
        if headless:
            options.headless = True
        _driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        _driver = webdriver.Firefox(executable_path=f"{drivers_folder}/geckodriver")
    elif browser_name == "yandex":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        service = ChromeService(executable_path=f"{drivers_folder}/yandexdriver")
        _driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "safari":
        _driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {browser_name} is not supported.")

    _driver.base_url = base_url
    _driver.maximize_window()

    yield _driver

    _driver.close()
