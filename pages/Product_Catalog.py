import time
from pages.Locator.Locators import Locators
from utils.Baseclass import BaseClass
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'product_catalog_page.log')


class ProductCatalog(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def navbar_selection(self):
        try:
            BaseClass.hover_element(self, Locators.product_catalog_navbar)
            BaseClass.impl_wait(self)
            BaseClass.exec_script_click(self, Locators.product_catalog_navbar_dropdown)
            BaseClass.impl_wait(self)
            # time.sleep(3)
            logger.info("Successfully selected the product catalog from the navbar.")
        except Exception as e:
            logger.error(f"Failed to select product catalog from navbar: {e}")
            raise

    def sort_asc(self):
        try:
            BaseClass.click_element(self, Locators.product_catalog_product_sort)
            BaseClass.click_element(self, Locators.product_catalog_product_sort_asc)
            BaseClass.impl_wait(self)
            # time.sleep(3)
            products = BaseClass.find_elements(self, Locators.product_catalog_product_list)
            logger.info("Sorted products in ascending order.")
            return [prods.text for prods in products]
        except Exception as e:
            logger.error(f"Failed to sort products in ascending order: {e}")
            raise

    def sort_desc(self):
        try:
            BaseClass.click_element(self, Locators.product_catalog_product_sort)
            BaseClass.click_element(self, Locators.product_catalog_product_sort_desc)
            BaseClass.impl_wait(self)
            # time.sleep(3)
            products = BaseClass.find_elements(self, Locators.product_catalog_product_sort_desc)
            logger.info("Sorted products in descending order.")
            return [prods.text for prods in products]
        except Exception as e:
            logger.error(f"Failed to sort products in descending order: {e}")
            raise

    def sort_price_asc(self):
        try:
            BaseClass.click_element(self, Locators.product_catalog_product_sort)
            BaseClass.click_element(self, Locators.product_catalog_product_sort_price_asc)
            BaseClass.impl_wait(self)
            # time.sleep(3)
            products = BaseClass.find_elements(self, Locators.product_catalog_product_sort_price_asc)
            logger.info("Sorted products by price in ascending order.")
            return [prods.text for prods in products]
        except Exception as e:
            logger.error(f"Failed to sort products by price ascending: {e}")
            raise

    def sort_price_desc(self):
        try:
            BaseClass.click_element(self, Locators.product_catalog_product_sort)
            BaseClass.click_element(self, Locators.product_catalog_product_sort_price_desc)
            BaseClass.impl_wait(self)
            # time.sleep(3)
            products = BaseClass.find_elements(self, Locators.product_catalog_product_sort_price_desc)
            logger.info("Sorted products by price in descending order.")
            return [prods.text for prods in products]
        except Exception as e:
            logger.error(f"Failed to sort products by price descending: {e}")
            raise

    def sort_rating_high(self):
        try:
            BaseClass.click_element(self, Locators.product_catalog_product_sort)
            BaseClass.click_element(self, Locators.product_catalog_product_sort_rating_high)
            BaseClass.impl_wait(self)
            # time.sleep(3)
            products = BaseClass.find_elements(self, Locators.product_catalog_product_sort_rating_high)
            logger.info("Sorted products by rating in high to low order.")
            return [prods.text for prods in products]
        except Exception as e:
            logger.error(f"Failed to sort products by rating high to low: {e}")
            raise

    def sort_rating_low(self):
        try:
            BaseClass.click_element(self, Locators.product_catalog_product_sort)
            BaseClass.click_element(self, Locators.product_catalog_product_sort_rating_low)
            BaseClass.impl_wait(self)
            # time.sleep(3)
            products = BaseClass.find_elements(self, Locators.product_catalog_product_sort_rating_low)
            logger.info("Sorted products by rating in low to high order.")
            return [prods.text for prods in products]
        except Exception as e:
            logger.error(f"Failed to sort products by rating low to high: {e}")
            raise

    def sort_date_new_old(self):
        try:
            BaseClass.click_element(self, Locators.product_catalog_product_sort)
            BaseClass.click_element(self, Locators.product_catalog_product_sort_date_new_old)
            BaseClass.impl_wait(self)
            # time.sleep(3)
            products = BaseClass.find_elements(self, Locators.product_catalog_product_sort_date_new_old)
            logger.info("Sorted products by date from new to old.")
            return [prods.text for prods in products]
        except Exception as e:
            logger.error(f"Failed to sort products by date from new to old: {e}")
            raise

    def sort_date_old_new(self):
        try:
            BaseClass.click_element(self, Locators.product_catalog_product_sort)
            BaseClass.click_element(self, Locators.product_catalog_product_sort_date_old_new)
            BaseClass.impl_wait(self)
            # time.sleep(3)
            products = BaseClass.find_elements(self, Locators.product_catalog_product_sort_date_old_new)

            logger.info("Sorted products by date from old to new.")
            return [prods.text for prods in products]
        except Exception as e:
            logger.error(f"Failed to sort products by date from old to new: {e}")
            raise
