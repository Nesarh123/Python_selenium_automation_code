import os
import time
import pytest
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

# ----------------------------
# Pytest Command Line Option
# ----------------------------
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

# ----------------------------
# Browser fixture
# ----------------------------
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

# ----------------------------
# WebDriver Setup Fixture
# ----------------------------
@pytest.fixture(scope="class")
def setup(request, browser):
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Invalid browser option.")

    driver.get("https://dev-os.rubick.ai/orders")
    driver.maximize_window()
    time.sleep(5)

    request.cls.driver = driver
    request.config._driver = driver  # store driver in config for hook access

    yield
    driver.quit()

# ----------------------------
# Screenshot Hook for pytest-html
# ----------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None) or getattr(item.config, "_driver", None)

        if driver:
            report_dir = os.path.dirname(item.config.option.htmlpath)
            screenshot_dir = os.path.join(report_dir, "Screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            safe_nodeid = re.sub(r'[^\w\d-]', '_', report.nodeid)
            file_name = f"{safe_nodeid}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            try:
                driver.save_screenshot(file_path)
                html = (
                    f'<div><img src="Screenshots/{file_name}" '
                    f'alt="screenshot" style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extras.append(pytest_html.extras.html(html))
            except Exception as e:
                print(f"Screenshot failed: {e}")

        report.extras = extras
# ----------------------------
# Custom HTML report title
# ----------------------------
def pytest_html_report_title(report):
    report.title = "Rubick Test Report"