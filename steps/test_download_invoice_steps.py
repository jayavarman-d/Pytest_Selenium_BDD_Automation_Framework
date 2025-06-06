import allure
import pytest
from utils.PageFactory import ObjectPage
from pytest_bdd import given, then, when, scenario
from tests.conftest import *
from utils.Loggers import setup_logger

logger = setup_logger(__name__, 'test_download_invoice_steps.log')


@pytest.mark.regression
@allure.feature('Filter Functionality')
@pytest.mark.usefixtures('browser_setup')
@pytest.mark.usefixtures('object_return')
@scenario(cart_feature, "Download Invoice and check it")
@allure.title('Validating Product Quantity Available')
@allure.story('Checking the requested Quantity is not available')
def test_download_invoice():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during product quantity functionality: {e}")
        pytest.fail(f"Test failed during product quantity functionality: {e}")


@given('User is on Homepage')
@allure.step('Given The User is on the Homepage')
def given_the_user_is_on_homepage(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User is on the homepage.")
    except Exception as e:
        logger.error(f"Failed to navigate to homepage: {e}")
        raise


@when('User clicks on signin')
@allure.step('When User clicks sign in')
def when_user_clicks_signin(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_path()
        logger.info("User clicked on the sign-in button.")
    except Exception as e:
        logger.error(f"Failed to click on sign-in button: {e}")
        raise


@when('User signin using Credentials')
@allure.step('And User signin using Credentials')
def and_user_signin_using_credentials(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_field_valid_username()
        page_obj.signin_field_valid_password()
        page_obj.signin_button()
        logger.info("User entered valid credentials and clicked sign-in.")
    except Exception as e:
        logger.error(f"Failed to enter credentials or click sign-in: {e}")
        raise


@when('User Clicks on Order History')
@allure.step('When User Clicks on Order History')
def when_user_clicks_on_order_history(browser_setup, object_return):
    try:
        page_obj = object_return.download_invoice(browser_setup)
        page_obj.order_history()
        logger.info("User clicks on order history")
    except Exception as e:
        logger.error(f"Failed to click order history: {e}")
        raise


@when('User clicks on view')
@allure.step('And User clicks on view')
def and_user_clicks_on_view(browser_setup, object_return):
    try:
        page_obj = object_return.download_invoice(browser_setup)
        page_obj.view_invoice()
        logger.info('User Clicks on View Invoice')
    except Exception as e:
        logger.error(f"Failed to view the Invoice: {e}")
        raise


@when('User clicks on Print')
@allure.step('When User clicks on Print')
def when_user_clicks_on_print(browser_setup, object_return):
    try:
        page_obj = object_return.download_invoice(browser_setup)
        page_obj.print_invoice()
        logger.info('User Successfully clicked print button in Page')
    except Exception as e:
        logger.error(f"Failed to click print button: {e}")
        raise


@when('User Clicks save in print Dialog')
@allure.step('And User Clicks save in print Dialog')
def and_user_clicks_save_in_print_dialog(browser_setup, object_return):
    try:
        page_obj = object_return.download_invoice(browser_setup)
        test_name = os.path.basename(__file__)
        page_obj.click_print_save(test_name)
        logger.info('User successfully downloaded the invoice')

    except Exception as e:
        logger.error(f"Failed to download the invoice: {e}")
        raise
