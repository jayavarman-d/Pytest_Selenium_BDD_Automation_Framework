from utils.Baseclass import BaseClass
from pages.Locator.Locators import Locators
from utils.Loggers import setup_logger
import openpyxl


workbook = openpyxl.load_workbook(filename='C:/Py/Selenium/Capstone_Ecommerce/test_data/Valid Data.xlsx')
sheet = workbook['signin']
logger = setup_logger(__name__, 'remove_cart_page.log')


class RemoveCart(BaseClass):

    def login(self):
        try:
            BaseClass.click_element(self, Locators.signin_page)
            BaseClass.click_element(self, Locators.signin_page_login_id)
            BaseClass.send_value(self, Locators.signin_page_login_id, sheet['A2'].value)
            BaseClass.click_element(self, Locators.signin_page_password)
            BaseClass.send_value(self, Locators.signin_page_password, sheet['B2'].value)
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

    def view_cart(self):
        try:
            BaseClass.hover_element(self, Locators.remove_cart_hover)
            BaseClass.click_element(self, Locators.remove_cart_hover_button)
            logger.info("Hovered over and clicked to view the cart.")
        except Exception as e:
            logger.error(f"Failed to view the cart: {e}")
            raise

    def remove_cart_item(self, test_name):
        try:
            initial = BaseClass.get_text(self, Locators.remove_cart_list_item)
            BaseClass.click_element(self, Locators.remove_cart_item)
            logger.info("Successfully removed item from the cart.")
            final = BaseClass.get_text(self, Locators.remove_cart_list_item)
            BaseClass.insert_test_data(self, test_name)
            return initial, final
        except Exception as e:
            logger.error(f"Failed to remove item from the cart: {e}")
            raise
