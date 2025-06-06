import allure
import pytest
from pytest_bdd import when, given, scenario, then
from openpyxl import *
from tests.conftest import *
from utils.PageFactory import ObjectPage
from utils.Loggers import setup_logger


workbook = load_workbook(filename='C:/Py/Selenium/Capstone_Ecommerce/test_data/Valid Data.xlsx')
sheet = workbook['signin']
logger = setup_logger(__name__, 'test_buy_wo_login.log')


@pytest.mark.complete_end
@pytest.mark.regression
@allure.feature('Full Purchase Flow')
@pytest.mark.usefixtures('browser_setup')
@pytest.mark.usefixtures('object_return')
@scenario(FullFlow_feature, "Full Flow from Login to Buying a product")
@allure.title('Full Flow')
@allure.story('Full Flow from Login to Buying a product')
def test_buy_wo_login():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during full purchase flow: {e}")
        pytest.fail(f"Test failed during full purchase flow: {e}")


@given('User is on Homepage')
@allure.step('Given User is on Homepage')
def given_user_on_homepage(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User is on the homepage.")
    except Exception as e:
        logger.error(f"Failed to navigate to homepage: {e}")
        raise


@when('User clicks sign in')
@allure.step('When User clicks sign in')
def when_user_clicks_signin(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_path()
        logger.info("User clicked on the sign-in button.")
    except Exception as e:
        logger.error(f"Failed to click on sign-in button: {e}")
        raise


@when('User should enter the credentials for login')
@allure.step('And User should enter the credentials for login')
def and_user_enter_credentials(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_field_valid_username()
        page_obj.signin_field_valid_password()
        page_obj.signin_button()
        logger.info("User entered valid credentials and clicked sign-in.")
    except Exception as e:
        logger.error(f"Failed to enter credentials or click sign-in: {e}")
        raise


@when('User successfully signed in and go to home')
@allure.step('When User successfully signed in and go to home')
def when_user_moves_to_home(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User successfully signed in and navigated to home.")
    except Exception as e:
        logger.error(f"Failed to navigate to home after sign-in: {e}")
        raise


@when('Navigate to Skincare')
@allure.step('And Navigate to Skincare')
def and_user_moves_to_navbar(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.nav_to_navbar()
        logger.info("User navigated to the skincare section in the navbar.")
    except Exception as e:
        logger.error(f"Failed to navigate to skincare section: {e}")
        raise


@when('User selects the Product')
@allure.step('When User selects the Product')
def when_user_select_product(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.product_select()
        logger.info("User selected a product.")
    except Exception as e:
        logger.error(f"Failed to select a product: {e}")
        raise


@when('Add the product to the cart')
@allure.step('And Add the product to the cart')
def and_user_add_product_to_cart(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.click_checkout()
        logger.info("User added the product to the cart.")
    except Exception as e:
        logger.error(f"Failed to add product to cart: {e}")
        raise


@when('Confirming the checkout')
@allure.step('When Confirming the checkout')
def when_user_confirm_the_checkout(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.checkout_cart_click()
        logger.info("User confirmed the checkout.")
    except Exception as e:
        logger.error(f"Failed to confirm the checkout: {e}")
        raise


@when('User Confirm Order')
@allure.step('And User Confirm Order')
def and_user_confirm_order(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.billing_checkout()
        logger.info("User confirmed the order during checkout.")
    except Exception as e:
        logger.error(f"Failed to confirm the order: {e}")
        raise


@then('the message "Your order has been Processed"')
@allure.step('Then the message "Your order has been Processed"')
def then_confirm_message_displays(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.confirmed_message()
        page_obj = ObjectPage().buy_without_login(browser_setup)
        test_name = os.path.basename(__file__)
        assert 'YOUR ORDER HAS BEEN PROCESSED!' in page_obj.confirm_order_message(test_name)
        logger.info("The confirmation message 'Your order has been Processed' is displayed.")
    except Exception as e:
        logger.error(f"Failed to display confirmation message: {e}")
        raise
