import allure
import pytest
from utils.PageFactory import ObjectPage
from pytest_bdd import when, then, given, scenario
from tests.conftest import *
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'test_product_bug.log')


@pytest.mark.regression
@allure.feature('Filter Functionality')
@pytest.mark.usefixtures('object_return')
@pytest.mark.usefixtures('browser_setup')
@scenario(product_inc_feature, "Product Selection Bug")
@allure.title('Validating Product Quantity Available')
@allure.story('Checking the requested Quantity is not available')
def test_prod_bug():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during product quantity functionality: {e}")
        pytest.fail(f"Test failed during product quantity functionality: {e}")


@given('The User is on the Homepage')
@allure.step('Given The User is on the Homepage')
def given_the_user_is_on_homepage(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User is on the homepage.")
    except Exception as e:
        logger.error(f"Failed to navigate to homepage: {e}")
        raise


@when('User navigates to Navbar and User selects the T-shirt Category')
@allure.step('User navigates to Navbar and User selects the T-shirt Category')
def when_user_navigate_to_navbar(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.navbar()
        page_obj.navbar_select()
        logger.info("User navigated to the navbar.")
    except Exception as e:
        logger.error(f"Failed to navigate to navbar: {e}")
        raise


@when('User select the Baseball T-shirt')
@allure.step('User select the Baseball T-shirt')
def and_user_selects_product(browser_setup, object_return):
    try:
        page_obj = object_return.product_page(browser_setup)
        page_obj.select_prods()
        logger.info("User selected the product.")
    except Exception as e:
        logger.error(f"Failed to select product: {e}")
        raise


@when('User selects the model')
@allure.step('User selects the model')
def and_user_clicks_size(browser_setup, object_return):
    try:
        page_obj = object_return.product_page(browser_setup)
        page_obj.select_size()
        logger.info("User clicked the add to cart button.")
    except Exception as e:
        logger.error(f"Failed to click add to cart: {e}")
        raise


@when('User clicks the add to cart')
@allure.step('User clicks the add to cart')
def and_user_clicks_add_cart(browser_setup, object_return):
    try:
        page_obj = object_return.product_page(browser_setup)
        test_name = os.path.basename(__file__)
        page_obj.select_checkout(test_name)
        logger.info("User clicked the add to cart button.")
    except Exception as e:
        logger.error(f"Failed to click add to cart: {e}")
        raise
