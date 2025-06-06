import allure
import pytest
from utils.PageFactory import ObjectPage
from pytest_bdd import when, then, given, scenario
from tests.conftest import *
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'test_prod_quantity.log')


@pytest.mark.regression
@allure.feature('Filter Functionality')
@pytest.mark.usefixtures('browser_setup')
@pytest.mark.usefixtures('object_return')
@scenario(cart_feature, "Checking the requested Quantity is not available")
@allure.title('Validating Product Quantity Available')
@allure.story('Checking the requested Quantity is not available')
def test_prod_quantity():
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


@when('User navigate to Skincare in Navbar and select Gift Ideas & Sets')
@allure.step('When User navigate to Skincare in Navbar and select Gift Ideas & Sets')
def when_user_navigate_to_navbar(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.nav_to_navbar()
        logger.info("User navigated to the navbar.")
    except Exception as e:
        logger.error(f"Failed to navigate to navbar: {e}")
        raise


@when('User Selects Night Care Crema Nera Obsidian Mineral Complex')
@allure.step('And User Selects Night Care Crema Nera Obsidian Mineral Complex')
def and_user_selects_product(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.product_select()
        logger.info("User selected the product.")
    except Exception as e:
        logger.error(f"Failed to select product: {e}")
        raise


@when('The User enters the quantity > availability into the quantity field')
@allure.step('When The User enters the quantity > availability into the quantity field')
def when_user_enters_the_quantity(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.product_quantity_verify()
        logger.info("User entered the quantity into the quantity field.")
    except Exception as e:
        logger.error(f"Failed to enter quantity: {e}")
        raise


@when('User clicks on the Add to Cart Button')
@allure.step('And User clicks on the Add to Cart Button')
def and_user_clicks_add_cart(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        page_obj.click_checkout()
        logger.info("User clicked the add to cart button.")
    except Exception as e:
        logger.error(f"Failed to click add to cart: {e}")
        raise


@then('User should not be able to checkout due to quantity higher than availability')
@allure.step('Then User cant able to checkout due to quantity higher than availability')
def then_user_cant_checkout(browser_setup, object_return):
    try:
        page_obj = object_return.product_cart(browser_setup)
        # test_name = os.path.basename(__file__)
        verify = page_obj.checkout_verify()
        assert 'Products marked with *** are not available in the desired quantity or out of stock!' in verify
        logger.info("User verified that they cannot checkout due to quantity being higher than availability.")
    except Exception as e:
        logger.error(f"Failed to verify checkout: {e}")
        raise

