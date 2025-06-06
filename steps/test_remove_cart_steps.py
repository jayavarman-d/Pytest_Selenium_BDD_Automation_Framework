import allure
import pytest
from pytest_bdd import given, then, when, scenario
from tests.conftest import *
from utils.PageFactory import ObjectPage
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'test_remove_cart.log')


@pytest.mark.regression
@allure.feature('Cart Functionality')
@pytest.mark.usefixtures('browser_setup')
@pytest.mark.usefixtures('object_return')
@scenario(cart_feature, "Remove items from the cart")
@allure.title('Validating that user buys without login')
@allure.story('Remove items from the cart')
def test_remove_cart():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during cart removal functionality: {e}")
        pytest.fail(f"Test failed during cart removal functionality: {e}")


@given('User Is on the Homepage')
@allure.step('Given User Is on the Homepage')
def given_user_on_homepage(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User is on the homepage.")
    except Exception as e:
        logger.error(f"Failed to navigate to homepage: {e}")
        raise


@when('User clicks on signin and signin using Credentials')
@allure.step('When User clicks on signin and signin using Credentials')
def when_user_clicks_signin_logs_in(browser_setup, object_return):
    try:
        page_obj = object_return.remove_cart(browser_setup)
        page_obj.login()
        logger.info("User signed in successfully.")
    except Exception as e:
        logger.error(f"Failed to sign in: {e}")
        raise


@when('User moves to the Homepage')
@allure.step('And User moves to the Homepage')
def and_user_move_to_home(browser_setup, object_return):
    try:
        page_obj = object_return.remove_cart(browser_setup)
        page_obj.move_to_home()
        logger.info("User navigated to the homepage after sign-in.")
    except Exception as e:
        logger.error(f"Failed to navigate to homepage: {e}")
        raise


@when('the user clicks the cart page')
@allure.step('When the user clicks the cart page')
def when_user_clicks_cart(browser_setup, object_return):
    try:
        page_obj = object_return.remove_cart(browser_setup)
        page_obj.view_cart()
        logger.info("User clicked on the cart page.")
    except Exception as e:
        logger.error(f"Failed to click cart page: {e}")
        raise


@when('starts to remove products from the cart')
@allure.step('And starts to remove products from the cart')
def and_user_removes_item(browser_setup, object_return):
    try:
        page_obj = object_return.remove_cart(browser_setup)
        test_name = os.path.basename(__file__)
        initial, final = page_obj.remove_cart_item(test_name)
        assert initial != final
        logger.info("User started removing items from the cart.")
    except Exception as e:
        logger.error(f"Failed to remove item from cart: {e}")
        raise
