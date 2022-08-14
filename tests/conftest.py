import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):  # custom command line argument
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        ser_obj = Service("/Users/sarve/PycharmProjects/chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)
    elif browser_name == "firefox":
        ser_obj = Service("/Users/sarve/PycharmProjects/geckodriver.exe")
        driver = webdriver.Firefox(service=ser_obj)
    elif browser_name == "edge":
        ser_obj = Service("/Users/sarve/PycharmProjects/msedgedriver.exe")
        driver = webdriver.Edge(service=ser_obj)

    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver  # assigning local driver to class driver to be used by the class
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
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
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
