import pytest
from selenium import webdriver
from pathlib import Path
import os
from os.path import abspath
import time

from selenium.webdriver.chrome.service import Service

driver = None


# Hook
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service = Service("../drivers/chromedriver")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.google.com")
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="..\\screenshots\\%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(screenshot_name):
    time.sleep(5)
    driver.get_screenshot_as_file('..\\screenshots\\%s' % screenshot_name)
