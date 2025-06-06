import allure
from utils.Baseclass import BaseClass
from pages.Locator.Locators import Locators
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'wishlist_page.log')


class ProductPage(BaseClass):

    def select_prods(self):
        try:
            BaseClass.click_element(self, Locators.product_page_product)
            logger.info("Selected product to cart.")

        except Exception as e:
            logger.error(f"Failed to select product to cart: {e}")
            raise

    def select_size(self):
        try:
            cart = BaseClass.find_element(self, Locators.product_page_product)
            BaseClass.exec_script_click(self, Locators.product_page_size)
            logger.info("Selecting Size")
            assert 'size' in cart
        except Exception as e:
            BaseClass.screenshot(self)
            allure.attach(f"Error: {e}", name="Size Selection Error", attachment_type=allure.attachment_type.TEXT)
            logger.error(f"Failed to selects the size : {e}")

    def select_checkout(self, test_name):
        try:
            BaseClass.click_element(self, Locators.product_quantity_add_to_cart)
            BaseClass.screenshot(self)
            BaseClass.insert_test_data(self, test_name)
            logger.info("Clicked 'Add to Cart' button.")
        except Exception as e:
            logger.error(f"Failed to click 'Add to Cart': {e}")
            raise
