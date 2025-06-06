import time
import openpyxl
from utils.Baseclass import BaseClass
from pages.Locator.Locators import Locators
from utils.Loggers import setup_logger


workbook = openpyxl.load_workbook(filename='C:/Py/Selenium/Capstone_Ecommerce/test_data/Valid Data.xlsx')
sheet = workbook['without_login']
logger = setup_logger(__name__, 'wishlist_page.log')


class Wishlist(BaseClass):

    def login(self):
        try:
            BaseClass.click_element(self, Locators.signin_page)
            BaseClass.click_element(self, Locators.signin_page_login_id)
            BaseClass.send_value(self, Locators.signin_page_login_id, sheet['A1'].value)
            BaseClass.click_element(self, Locators.signin_page_password)
            BaseClass.send_value(self, Locators.signin_page_password, sheet['B1'].value)
            BaseClass.click_element(self, Locators.signin_page_button)
            logger.info("Successfully logged in with valid credentials.")
        except Exception as e:
            logger.error(f"Failed to log in: {e}")
            raise

    def move_to_home(self):
        try:
            BaseClass.click_element(self, Locators.home_path)
            logger.info("Successfully navigated to the homepage.")
        except Exception as e:
            logger.error(f"Failed to navigate to the homepage: {e}")
            raise

    def select_prods(self):
        try:
            BaseClass.click_element(self, Locators.wishlist_product)
            logger.info("Selected product for wishlist.")
        except Exception as e:
            logger.error(f"Failed to select product for wishlist: {e}")
            raise

    def add_to_wishlist(self):
        try:
            BaseClass.click_element(self, Locators.wishlist_product_button)
            logger.info("Successfully added product to wishlist.")
        except Exception as e:
            logger.error(f"Failed to add product to wishlist: {e}")
            raise

    def go_to_profile_hover(self):
        try:
            BaseClass.hover_element(self, Locators.wishlist_product_profile_hover)
            logger.info("Hovered over the profile section.")
        except Exception as e:
            logger.error(f"Failed to hover over profile section: {e}")
            raise

    def go_to_wishlist(self):
        try:
            BaseClass.click_element(self, Locators.wishlist_product_profile_hover_dropdown)
            BaseClass.impl_wait(self)
            logger.info("Navigated to the wishlist page.")
        except Exception as e:
            logger.error(f"Failed to navigate to wishlist: {e}")
            raise

    def remove_from_the_wishlist(self, test_name):
        try:
            BaseClass.click_element(self, Locators.wishlist_product_remove)
            BaseClass.impl_wait(self)
            BaseClass.insert_test_data(self, test_name)
            logger.info("Successfully removed product from wishlist.")
        except Exception as e:
            logger.error(f"Failed to remove product from wishlist: {e}")
            raise
