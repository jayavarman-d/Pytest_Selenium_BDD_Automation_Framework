from pages.Homepage import HomePage
from pages.Product_Catalog import ProductCatalog
from pages.Product_Cart import ProductCart
from pages.Wishlist import Wishlist
from pages.Remove_Cart import RemoveCart
from pages.Buy_Without_Login import BuyWithoutLogin
from pages.Download_Invoice import DownloadInvoice
from pages.Productpage import ProductPage


class ObjectPage:

    def home_page(self, driver):
        return HomePage(driver)

    def product_catalog_page(self, driver):
        return ProductCatalog(driver)

    def product_cart(self, driver):
        return ProductCart(driver)

    def wishlist(self, driver):
        return Wishlist(driver)

    def remove_cart(self, driver):
        return RemoveCart(driver)

    def buy_without_login(self, driver):
        return BuyWithoutLogin(driver)

    def download_invoice(self, driver):
        return DownloadInvoice(driver)

    def product_page(self, driver):
        return ProductPage(driver)
