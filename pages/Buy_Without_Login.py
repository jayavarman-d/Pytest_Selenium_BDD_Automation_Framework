from utils.Baseclass import BaseClass
import datetime
from pages.Locator.Locators import Locators
from utils.Loggers import setup_logger
import openpyxl


workbook = openpyxl.load_workbook(filename='C:/Py/Selenium/Capstone_Ecommerce/test_data/Valid Data.xlsx')
sheet = workbook['without_login']
logger = setup_logger(__name__, 'buy_without_login_page.log')


class BuyWithoutLogin(BaseClass):

    def add_to_cart(self):
        try:
            BaseClass.click_element(self, Locators.buy_without_login_add_cart)
            logger.info("Product added to cart.")
        except Exception as e:
            logger.error(f"Failed to add product to cart: {e}")
            raise

    def checkout_product(self):
        try:
            BaseClass.click_element(self, Locators.buy_without_login_checkout)
            logger.info("Clicked on checkout.")
        except Exception as e:
            logger.error(f"Failed to proceed to checkout: {e}")
            raise

    def select_guest_account(self):
        try:
            BaseClass.click_element(self, Locators.buy_without_login_guest)
            BaseClass.click_element(self, Locators.buy_without_login_guest_button)
            logger.info("Selected guest account and proceeded.")
        except Exception as e:
            logger.error(f"Failed to select guest account: {e}")
            raise

    def enter_details(self):
        try:
            BaseClass.send_value(self, Locators.wo_login_paths(self, 'firstname'), sheet['A1'].value)
            BaseClass.send_value(self, Locators.wo_login_paths(self, 'lastname'), sheet['B1'].value)
            BaseClass.send_value(self, Locators.wo_login_paths(self, "email' and @id='guestFrm_email"), sheet['C1'].value)
            BaseClass.send_value(self, Locators.wo_login_paths(self, 'telephone'), sheet['D1'].value)
            BaseClass.send_value(self, Locators.wo_login_paths(self, 'fax'), sheet['E1'].value)
            BaseClass.send_value(self, Locators.wo_login_paths(self, 'company'), sheet['F1'].value)
            BaseClass.send_value(self, Locators.wo_login_paths(self, 'address_1'), sheet['G1'].value)
            BaseClass.send_value(self, Locators.wo_login_paths(self, 'city'), sheet['H1'].value)
            BaseClass.click_element(self, Locators.wo_login_paths_select(self, "country_id']//option[text() ='France"))
            BaseClass.click_element(self, Locators.wo_login_paths_select(self, "zone_id']//option[text() ='Paris / Ill de France"))
            BaseClass.send_value(self, Locators.wo_login_paths(self, 'postcode'), sheet['I1'].value)
            BaseClass.click_element(self, Locators.buy_without_login_guest_confirm)
            logger.info("Entered guest details successfully.")
        except Exception as e:
            logger.error(f"Failed to enter guest details: {e}")
            raise

    def checkout_confirmation(self):
        try:
            amount_text = BaseClass.get_text(self, Locators.buy_without_login_guest_amount)
            amount = amount_text.replace('$', '')
            amount_val = float(amount)
            BaseClass.insert_data_invoice(self, amount_val)
            logger.info('Entered the invoice details into the database')
            BaseClass.click_element(self, Locators.buy_without_login_guest_confirm_checkout)
            logger.info("Confirmed checkout.")
        except Exception as e:
            logger.error(f"Failed to confirm checkout: {e}")
            raise

    def confirm_order_message(self, test_name):
        try:
            text = BaseClass.get_text(self, Locators.buy_without_login_guest_confirm_message)
            BaseClass.insert_test_data(self, test_name)
            return text
        except Exception as e:
            logger.error(f"Failed to fetch confirm message: {e}")
