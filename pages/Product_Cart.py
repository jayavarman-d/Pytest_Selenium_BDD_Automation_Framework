import time
import re
from utils.Baseclass import BaseClass
from pages.Locator.Locators import Locators
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'product_cart_page.log')


class ProductCart(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def nav_to_navbar(self):
        try:
            BaseClass.hover_element(self, Locators.product_quantity_nav_skincare)
            BaseClass.click_element(self, Locators.product_quantity_nav_hover_dropdown)
            logger.info("Navigated to the skincare section in the navbar.")
        except Exception as e:
            logger.error(f"Failed to navigate to navbar: {e}")
            raise

    def product_select(self):
        try:
            BaseClass.click_element(self, Locators.product_quantity_select)
            logger.info("Selected the product.")
        except Exception as e:
            logger.error(f"Failed to select the product: {e}")
            raise

    def product_quantity_verify(self):
        try:
            element = BaseClass.get_text(self, Locators.product_quantity_getter)
            quantity_text = element.strip()
            qty = int(re.search(r'\d+', quantity_text).group())
            BaseClass.send_value(self, Locators.product_quantity_field, qty + 1)
            logger.info(f"Verified product quantity: {qty}, and entered quantity: {qty + 1}.")
        except Exception as e:
            logger.error(f"Failed to verify or update the product quantity: {e}")
            raise

    def click_invalid_checkout(self):
        try:
            BaseClass.click_element(self, Locators.product_quantity_add_to_cart)
            logger.info("Clicked 'Add to Cart' button.")
        except Exception as e:
            logger.error(f"Failed to click 'Add to Cart': {e}")
            raise

    def click_checkout(self):
        try:
            BaseClass.click_element(self, Locators.product_quantity_add_to_cart)
            logger.info("Clicked 'Add to Cart' button.")
        except Exception as e:
            logger.error(f"Failed to click 'Add to Cart': {e}")
            raise

    def checkout_verify(self):
        try:
            BaseClass.click_element(self, Locators.product_quantity_checkout)
            confirmation_text = BaseClass.get_text(self, Locators.product_quantity_checkout_confirm_message)
            logger.info(f"Checkout initiated. Confirmation message: {confirmation_text}")
            return confirmation_text
        except Exception as e:
            logger.error(f"Failed to initiate checkout or retrieve confirmation message: {e}")
            raise

    def checkout_cart_click(self):
        try:
            BaseClass.click_element(self, Locators.product_quantity_checkout)
            logger.info("Clicked on checkout cart.")
        except Exception as e:
            logger.error(f"Failed to click on checkout cart: {e}")
            raise

    def billing_checkout(self):
        try:
            BaseClass.click_element(self, Locators.product_quantity_checkout_confirm)
            logger.info("Confirmed the checkout.")
        except Exception as e:
            logger.error(f"Failed to confirm the checkout: {e}")
            raise

    def confirmed_message(self):
        try:
            confirmation_message = BaseClass.get_text(self, Locators.order_confirm_message)
            logger.info(f"Order confirmed with message: {confirmation_message}")
        except Exception as e:
            logger.error(f"Failed to get order confirmation message: {e}")
            raise
