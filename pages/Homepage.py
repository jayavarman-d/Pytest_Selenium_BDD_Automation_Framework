import time
import openpyxl
from pages.Locator.Locators import Locators
from utils.Baseclass import BaseClass
from utils.Loggers import setup_logger


workbook = openpyxl.load_workbook(filename='C:/Py/Selenium/Capstone_Ecommerce/test_data/Valid Data.xlsx')
sheet = workbook['signin']
logger = setup_logger(__name__, 'homepage_page.log')


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def signin_path(self):
        try:
            element = BaseClass.find_element(self, Locators.signin_page)
            BaseClass.click_element(self, element)
            logger.info("Navigated to Sign-In Page.")
        except Exception as e:
            logger.error(f"Failed to navigate to Sign-In Page: {e}")
            raise

    def signin_field_username(self, username):
        try:
            BaseClass.send_value(self, Locators.signin_page_login_id, username)
            logger.info("Entered username in the Sign-In field.")
        except Exception as e:
            logger.error(f"Failed to enter username: {e}")
            raise

    def signin_field_password(self, password):
        try:
            BaseClass.send_value(self, Locators.signin_page_password, password)
            logger.info("Entered password in the Sign-In field.")
        except Exception as e:
            logger.error(f"Failed to enter password: {e}")
            raise

    def signin_button(self):
        try:
            BaseClass.click_element(self, Locators.signin_page_button)
            logger.info("Clicked the Sign-In button.")
        except Exception as e:
            logger.error(f"Failed to click the Sign-In button: {e}")
            raise

    def signin_fail_text(self):
        try:
            text = BaseClass.get_text(self, Locators.signin_failed_text)
            BaseClass.impl_wait(self)
            # BaseClass.insert_test_data(self, test_name)
            logger.info(f"Sign-In failed with message: {text}")
            return text
        except Exception as e:
            logger.error(f"Failed to get Sign-In failure text: {e}")
            raise

    def signin_field_valid_username(self):
        try:
            BaseClass.clear_text(self, Locators.signin_page_login_id)
            BaseClass.send_value(self, Locators.signin_page_login_id, sheet['A1'].value)
            logger.info("Entered valid username in the Sign-In field.")
        except Exception as e:
            logger.error(f"Failed to enter valid username: {e}")
            raise

    def signin_field_valid_password(self):
        try:
            BaseClass.clear_text(self, Locators.signin_page_password)
            BaseClass.send_value(self, Locators.signin_page_password, sheet['B1'].value)
            logger.info("Entered valid password in the Sign-In field.")
        except Exception as e:
            logger.error(f"Failed to enter valid password: {e}")
            raise

    def signin_pass_text(self):
        try:
            text = BaseClass.get_text(self, Locators.signin_pass_text)
            BaseClass.impl_wait(self)
            logger.info(f"Sign-In failed with message: {text}")
            return text
        except Exception as e:
            logger.error(f"Failed to get Sign-In failure text: {e}")
            raise

    def home_path(self):
        try:
            BaseClass.click_element(self, Locators.home_path)
            BaseClass.impl_wait(self)
            logger.info("Navigated to the Home Page.")
        except Exception as e:
            logger.error(f"Failed to navigate to the Home Page: {e}")
            raise

    def navbar(self):
        try:
            BaseClass.hover_element(self, Locators.home_navbar_hover)
            BaseClass.impl_wait(self)
            logger.info("Hovered over the navbar.")
        except Exception as e:
            logger.error(f"Failed to hover over the navbar: {e}")
            raise

    def navbar_select(self):
        try:
            BaseClass.exec_script_click(self, Locators.home_navbar_hover_dropdown)
            BaseClass.impl_wait(self)
            logger.info("Selected option from the navbar dropdown.")
        except Exception as e:
            logger.error(f"Failed to select option from navbar dropdown: {e}")
            raise

    def navbar_assert(self):
        try:
            text = BaseClass.get_text(self, Locators.home_navbar_category)
            # BaseClass.insert_test_data(self, test_name)
            return text
        except Exception as e:
            logger.error(f"Failed to fetch confirm message: {e}")

    def searchbar(self):
        try:
            BaseClass.click_element(self, Locators.home_search_bar)
            BaseClass.send_value(self, Locators.home_search_bar, 'Shirts')
            logger.info("Searched for 'Shirts' in the search bar.")
        except Exception as e:
            logger.error(f"Failed to interact with the search bar: {e}")
            raise

    def search_product(self):
        try:
            BaseClass.click_element(self, Locators.home_search_bar_icon)
            logger.info("Clicked the search button and searched the product.")
        except Exception as e:
            logger.error(f"Failed to search the product: {e}")
            raise

    def search_assert(self):
        try:
            text = BaseClass.get_text(self, Locators.home_search_assert)
            # BaseClass.insert_test_data(self, test_name)
            return text
        except Exception as e:
            logger.error(f"Failed to fetch confirm message: {e}")

