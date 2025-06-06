import allure
import os
import pytest
from pytest_bdd import scenario, given, when, then
from utils.PageFactory import ObjectPage
from utils.Loggers import setup_logger
from tests.conftest import *

logger = setup_logger(__name__, 'test_buy_without_login.log')


@pytest.mark.complete_end
@pytest.mark.regression
@allure.feature('Cart Functionality')
@pytest.mark.usefixtures('browser_setup')
@pytest.mark.usefixtures('object_return')
@scenario(cart_feature, "The User should be able to buy a product without being logged in but the details"
                        " should be collected")
@allure.story('Users buys product without logging in')
@allure.title('Users can buy Product without logging in')
def test_buy_wo_login_scenario():
    pass


@given("User is on Homepage")
@allure.step('Given User is on Homepage')
def given_user_on_homepage(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User is on the homepage.")
    except Exception as e:
        logger.error(f"Failed to navigate to the homepage: {e}")
        raise


@when("User moves to Navbar")
@allure.step('When User moves to Navbar')
def when_user_moves_to_navbar(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.nav_to_navbar()
        logger.info("User navigated to the navbar.")
    except Exception as e:
        logger.error(f"Failed to move to navbar: {e}")
        raise


@when("User selects the Product")
@allure.step('And User selects the Product')
def and_user_select_product(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.product_select()
        logger.info("User selected the product.")
    except Exception as e:
        logger.error(f"Failed to select product: {e}")
        raise


@when("User adds the Product to Cart")
@allure.step('And User adds the Product to Cart')
def when_user_adds_cart(browser_setup, object_return):
    try:
        page_obj = object_return.buy_without_login(browser_setup)
        page_obj.add_to_cart()
        page_obj.checkout_product()
        logger.info("User added the product to cart and proceeded to checkout.")
    except Exception as e:
        logger.error(f"Failed to add product to cart or checkout: {e}")
        raise


@when("User selects Guest Account")
@allure.step('And User selects Guest Account')
def and_user_selects_guest_account(browser_setup, object_return):
    try:
        page_obj = object_return.buy_without_login(browser_setup)
        page_obj.select_guest_account()
        logger.info("User selected guest account for checkout.")
    except Exception as e:
        logger.error(f"Failed to select guest account: {e}")
        raise


@when("User enters required details for the shipping (mail,name,company,street,city)")
@allure.step('When User enters required details for the shipping (mail,name,company,street,city)')
def when_user_enters_required_details(browser_setup, object_return):
    try:
        page_obj = object_return.buy_without_login(browser_setup)
        page_obj.enter_details()
        logger.info("User entered the required shipping details.")
    except Exception as e:
        logger.error(f"Failed to enter required details: {e}")
        raise


@when("User enters into the payment method and Checkout")
@allure.step('And User enters into the payment method and Checkout')
def and_user_enters_into_payment(browser_setup, object_return):
    try:
        page_obj = object_return.buy_without_login(browser_setup)
        page_obj.checkout_confirmation()
        test_name = os.path.basename(__file__)
        assert 'YOUR ORDER HAS BEEN PROCESSED!' in page_obj.confirm_order_message(str(test_name))
        logger.info("User completed the payment process and confirmed checkout.")
    except Exception as e:
        logger.error(f"Failed to enter payment details or confirm checkout: {e}")
        raise

