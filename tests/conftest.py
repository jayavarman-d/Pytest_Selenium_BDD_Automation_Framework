import configparser
import os.path
import pyodbc
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.PageFactory import ObjectPage
from utils.Loggers import setup_logger

logger = setup_logger(__name__, 'conftest.log')

@pytest.fixture(scope='class')
def browser_setup(request):
    options_add = Options()
    options_add.add_argument('--start-maximized')
    options_add.add_argument('--disable-popup-blocking')
    # options_add.add_argument('--kiosk-printing')
    options_add.add_argument(f'--print-to-pdf=C:/Users/jayavarman.durai/Downloads/')
    options_add.add_argument('--disable-extensions')
    options_add.add_argument('--no-sandbox')
    options_add.add_argument('--disable-gpu')

    prefs = {
        "printing.print_preview_sticky_settings": False,
        "savefile.default_directory": "C:\\Users\\jayavarman.durai\\Downloads"
    }
    options_add.add_experimental_option("prefs", prefs)

    driver_path = "C:\\Users\\jayavarman.durai\\Downloads\\chromedriver-win64\\chromedriver.exe"
    service_add = Service(driver_path)
    driver = webdriver.Chrome(service=service_add, options=options_add)
    driver.get("https://automationteststore.com/")

    yield driver
    driver.close()


@pytest.fixture(scope='module')
def object_return():
    return ObjectPage()



# def pytest_sessionstart(session):
#     logger.info("Test session is starting...")
#
#
# def pytest_sessionfinish(session, exitstatus):
#     logger.info("Test session has finished.")
#     if exitstatus == 0:
#         logger.info("All tests passed successfully.")
#         allure.attach("Session End", "All tests passed successfully", allure.attachment_type.TEXT)
#     else:
#         logger.error("Some tests failed.")
#         allure.attach("Session End", "Some tests failed", allure.attachment_type.TEXT)
#
#
# # @pytest.hookimpl(tryfirst=True)
# def dbconnect():
#     config = configparser.ConfigParser()
#     config.read('C:/Py/Selenium/Capstone_Ecommerce_Updated/dbconfig.ini')
#     db = config['database']
#     driver = db['DRIVER']
#     server = db['Server']
#     database = db['Database']
#     connection = db['Trusted_Connection']
#     conn = pyodbc.connect(
#         f"DRIVER={{{driver}}};"
#         f"Server={server};"
#         f"Database={database};"
#         f"Trusted_Connection={connection};"
#     )
#     cursor = conn.cursor()
#
#
# # @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_protocol(item, nextitem):
#     logger.info(f"Running test: {item.nodeid}")
#     allure.attach(f"Running Test: {item.nodeid}", f"Running test {item.nodeid}", allure.attachment_type.TEXT)
#     return None
#
#
# def pytest_runtest_logreport(report):
#     if report.outcome == 'failed':
#         logger.error(f"Test failed: {report.nodeid}")
#         allure.attach(f"Test failed: {report.nodeid}", f"Test {report.nodeid} failed", allure.attachment_type.TEXT)
#     elif report.outcome == 'passed':
#         logger.info(f"Test passed: {report.nodeid}")
#         allure.attach(f"Test passed: {report.nodeid}", f"Test {report.nodeid} passed", allure.attachment_type.TEXT)
#     else:
#         logger.warning(f"Test skipped or error: {report.nodeid}")
#         allure.attach(f"Test skipped: {report.nodeid}", f"Test {report.nodeid} skipped or errored", allure.attachment_type.TEXT)
#
#
# def pytest_fixture_setup(fixturedef):
#     logger.info(f"Setting up fixture: {fixturedef.scope} - {fixturedef.name}")
#     allure.attach(f"Setting up fixture: {fixturedef.name}", f"Fixture {fixturedef.name} is being set up", allure.attachment_type.TEXT)
#
#
# def pytest_fixture_post_finalizer(fixturedef):
#     logger.info(f"Tearing down fixture: {fixturedef.scope} - {fixturedef.name}")
#     allure.attach(f"Tearing down fixture: {fixturedef.name}", f"Fixture {fixturedef.name} is being torn down", allure.attachment_type.TEXT)
#



# @pytest.fixture(scope='class')
# @pytest.param(['edge','chrome'])
# def crossbrowser_setup(request):
#     options_add = Options()
#     options_add.add_argument('--start-maximized')
#     options_add.add_argument('--disable-popup-blocking')
#     # options_add.add_argument('--kiosk-printing')
#     options_add.add_argument(f'--print-to-pdf=C:/Users/jayavarman.durai/Downloads/')
#     options_add.add_argument('--disable-extensions')
#     options_add.add_argument('--no-sandbox')
#     options_add.add_argument('--disable-gpu')
#
#     prefs = {
#         "printing.print_preview_sticky_settings": False,
#         "savefile.default_directory": "C:\\Users\\jayavarman.durai\\Downloads"
#     }
#     options_add.add_experimental_option("prefs", prefs)
#
#     driver_path = 'C:/Users/jayavarman.durai/Downloads/chromedriver-win64/chromedriver.exe'
#     service_add = Service(driver_path)
#     driver = webdriver.Chrome(service=service_add, options=options_add)
#     driver.get("https://automationteststore.com/")
#
#     yield driver
#     driver.close()


__dir = os.path.dirname(os.path.realpath(__file__))
cart_feature = os.path.join(os.path.dirname(os.path.realpath(__dir)), "Features", "cart.feature")
FullFlow_feature = os.path.join(os.path.dirname(os.path.realpath(__dir)), "Features", "FullFlow.feature")
login_feature = os.path.join(os.path.dirname(os.path.realpath(__dir)), "Features", "login.feature")
Navigation_feature = os.path.join(os.path.dirname(os.path.realpath(__dir)), "Features", "Navigation Bar and Home.feature")
product_inc_feature = os.path.join(os.path.dirname(os.path.realpath(__dir)), "Features", "Product Inc.feature")
search_filter_feature = os.path.join(os.path.dirname(os.path.realpath(__dir)), "Features", "Filter.feature")

