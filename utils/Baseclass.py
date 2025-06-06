from datetime import datetime
import configparser
import allure
import time, os
import pytest
import pyautogui
from selenium.webdriver.common.by import By
from utils.dbconnection import DatabaseCon
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from utils.Loggers import setup_logger


logger = setup_logger('base_class_logger', 'base_class.log')


@pytest.mark.usefixtures('browser_setup')
class BaseClass(DatabaseCon):

    def __init__(self, driver):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.driver = driver
        self.ac = ActionChains(driver)

    def wait_for_element(self, locator, condition, timeout=10):

        try:
            if isinstance(locator, WebElement):
                return locator
            by, path = locator
            logger.info(f"Waiting for element: {path}")
            return WebDriverWait(self.driver, timeout).until(condition((by, path)))
        except Exception as e:
            logger.error(f"Failed to find element: {locator} with condition {condition}: {str(e)}")
            raise

    def find_element(self, locator):

        try:
            element = self.wait_for_element(locator, ex.visibility_of_element_located)
            logger.info(f"Found element: {locator}")
            return element
        except Exception as e:
            logger.error(f"Error in finding element: {locator} - {str(e)}")
            raise

    def find_elements(self, locator):

        try:
            elements = self.wait_for_element(locator, ex.presence_of_all_elements_located)
            logger.info(f"Found elements: {locator}")
            return elements
        except Exception as e:
            logger.error(f"Error in finding elements: {locator} - {str(e)}")
            raise

    def click_element(self, locator):

        try:
            element = self.wait_for_element(locator, ex.element_to_be_clickable)
            element.click()
            logger.info(f"Clicked on element: {locator}")
        except Exception as e:
            logger.error(f"Error in clicking element: {locator} - {str(e)}")
            raise

    def send_value(self, locator, value):

        try:
            element = self.wait_for_element(locator, ex.element_to_be_clickable)
            element.send_keys(value)
            logger.info(f"Sent value to element: {locator} with value: {value}")
        except Exception as e:
            logger.error(f"Error in sending value to element: {locator} - {str(e)}")
            raise

    def get_text(self, locator):

        try:
            element = self.wait_for_element(locator, ex.visibility_of_element_located)
            text = element.text
            logger.info(f"Got text from element: {locator} - Text: {text}")
            return text
        except Exception as e:
            logger.error(f"Error in getting text from element: {locator} - {str(e)}")
            raise

    def clear_text(self, locator):

        try:
            element = self.wait_for_element(locator, ex.element_to_be_clickable)
            element.clear()
            logger.info(f"Cleared text of element: {locator}")
        except Exception as e:
            logger.error(f"Error in clearing text from element: {locator} - {str(e)}")
            raise

    def impl_wait(self):

        self.driver.implicitly_wait(5)
        logger.info("Implicit wait for 5 seconds.")

    def hover_element(self, locator):

        try:
            element = self.wait_for_element(locator, ex.visibility_of_element_located)
            ac = ActionChains(self.driver)
            ac.move_to_element(element).perform()
            logger.info(f"Hovered over element: {locator}")
        except Exception as e:
            logger.error(f"Error in hovering over element: {locator} - {str(e)}")
            raise

    def exec_script_click(self, locator):

        try:
            element = self.wait_for_element(locator, ex.presence_of_element_located)
            self.driver.execute_script('arguments[0].click()', element)
            logger.info(f"Executed script click on element: {locator}")
        except Exception as e:
            logger.error(f"Error in executing script click on element: {locator} - {str(e)}")
            raise

    def wait_page(self):
        try:
            time.sleep(3)
            logger.info("Waited for 3 seconds.")
        except Exception as e:
            logger.error(f"Error waiting/sleeping the page {e}")

    def click_save_print(self):
        try:
            self.wait_page()
            pyautogui.click(x=1544, y=261)
            pyautogui.click(x=1492, y=339)
            self.wait_page()
            pyautogui.click(x=1497, y=1019)
            self.wait_page()
            pyautogui.click(x=684, y=668)
            self.wait_page()
            logger.info('Successfully saved the invoice file through the Print Dialog')
        except Exception as e:
            logger.error(f"Error selecting and saving the invoice in the System {e}")

    def screenshot(self):

        try:
            path = 'C:/Py/Selenium/Capstone_Ecommerce/reports/screenshots'
            if not os.path.exists(path):
                os.makedirs(path)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screens = os.path.join(path, f"screen_{stamp}.png")
            self.driver.save_screenshot(screens)
            logger.info(f"Screenshot Saved Successfully")
            with open(screens, "rb") as file:
                allure.attach(file.read(), name=f"Screenshot_{stamp}", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logger.error(f"Error in taking screenshot")
            raise

    def insert_data_invoice(self, amount):
        try:
            query = f'INSERT INTO invoice VALUES(?,?)'
            self.cursor.execute(query, (amount, datetime.now()))
            self.conn.commit()
            logger.info(f'Invoice data successfully entered into the database')
        except Exception as e:
            logger.error(f'The invoice details is not getting inserted into the table: {e}')

    def insert_test_data(self, test_name):
        try:
            query = f'INSERT INTO test_run VALUES(?,?)'
            self.cursor.execute(query, (test_name, datetime.now()))
            self.conn.commit()
            logger.info('The test details is entered into the database')
        except Exception as e:
            logger.error(f'The test_data is not getting inserted into the table: {e}')

