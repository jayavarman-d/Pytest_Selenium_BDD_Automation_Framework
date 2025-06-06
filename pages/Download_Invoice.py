import os
from utils.Baseclass import BaseClass
from pages.Locator.Locators import Locators
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'download_invoice_page.log')


class DownloadInvoice(BaseClass):

    def order_history(self):
        try:
            BaseClass.click_element(self, Locators.download_invoice_order_history)
            logger.info("Navigated to Order History.")
        except Exception as e:
            logger.error(f"Failed to navigate to Order History: {e}")
            raise

    def view_invoice(self):
        try:
            BaseClass.click_element(self, Locators.download_invoice_view)
            logger.info("Viewed the invoice.")
        except Exception as e:
            logger.error(f"Failed to view the invoice: {e}")
            raise

    def print_invoice(self):
        try:
            BaseClass.click_element(self, Locators.download_invoice_print)
            logger.info("Printed the invoice.")
        except Exception as e:
            logger.error(f"Failed to print the invoice: {e}")
            raise

    def click_print_save(self, test_name):
        try:
            BaseClass.click_save_print(self)
            BaseClass.insert_test_data(self, test_name)
            logger.info("Saved the invoice.")
        except Exception as e:
            logger.error(f"Failed to save the invoice: {e}")
            raise
