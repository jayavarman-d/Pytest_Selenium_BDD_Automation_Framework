import allure
import pytest
from utils.PageFactory import ObjectPage
from pytest_bdd import given, then, when, scenario
from tests.conftest import *
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'test_wishlist.log')


@pytest.mark.regression
@allure.feature('Product Interaction')
@pytest.mark.usefixtures('browser_setup')
@pytest.mark.usefixtures('object_return')
@scenario(product_inc_feature, "Checking add to Wishlist and remove is working or not")
@allure.title('Validating Wishlist page')
@allure.story('Checking add to Wishlist and remove is working or not')
def test_wishlist():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during wishlist functionality: {e}")
        pytest.fail(f"Test failed during wishlist functionality: {e}")


@given('User is on the homepage')
@allure.step('Given User user is on the homepage')
def given_user_on_homepage(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User is on the homepage.")
    except Exception as e:
        logger.error(f"Failed to navigate to homepage: {e}")
        raise


@when('User clicks on login and move to login page')
@allure.step('When User clicks on login and move to login page')
def when_user_click_login(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_path()
        logger.info("User clicked on the login page.")
    except Exception as e:
        logger.error(f"Failed to click login: {e}")
        raise


@when('User logs using username and password')
@allure.step('And User logs using username and password')
def and_the_user_logs_using_username(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_field_valid_username()
        page_obj.signin_field_valid_password()
        page_obj.signin_button()
        logger.info("User successfully logged in.")
    except Exception as e:
        logger.error(f"Failed to log in with valid credentials: {e}")
        raise


@when('User moves to Homepage')
@allure.step('When User moves to Homepage')
def when_user_moves_to_homepage(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User navigated to homepage after login.")
    except Exception as e:
        logger.error(f"Failed to navigate to homepage: {e}")
        raise


@when('The user is on a product page and select it')
@allure.step('And The user is on a product page and select it')
def and_user_selects_product(browser_setup, object_return):
    try:
        page_obj = object_return.wishlist(browser_setup)
        page_obj.select_prods()
        logger.info("User selected a product.")
    except Exception as e:
        logger.error(f"Failed to select product: {e}")
        raise


@when('Added a product to wishlist')
@allure.step('When Added a product to wishlist')
def when_user_adds_to_wishlist(browser_setup, object_return):
    try:
        page_obj = object_return.wishlist(browser_setup)
        page_obj.add_to_wishlist()
        logger.info("Product added to wishlist.")
    except Exception as e:
        logger.error(f"Failed to add product to wishlist: {e}")
        raise


@when('User Go to Profile')
@allure.step('And User Go to Profile')
def and_user_visits_profile(browser_setup, object_return):
    try:
        page_obj = object_return.wishlist(browser_setup)
        page_obj.go_to_profile_hover()
        logger.info("User navigated to profile.")
    except Exception as e:
        logger.error(f"Failed to navigate to profile: {e}")
        raise


@when('User selects wishlist')
@allure.step('When User selects wishlist')
def when_user_selects_wishlist(browser_setup, object_return):
    try:
        page_obj = object_return.wishlist(browser_setup)
        page_obj.go_to_wishlist()
        logger.info("User navigated to wishlist.")
    except Exception as e:
        logger.error(f"Failed to navigate to wishlist: {e}")
        raise


@when('User was able to view the products which were added and removes it')
@allure.step('And User was able to view the products which were added and removes it')
def and_user_visits_wishlist_remove(browser_setup, object_return):
    try:
        page_obj = object_return.wishlist(browser_setup)
        test_name = os.path.basename(__file__)
        page_obj.remove_from_the_wishlist(test_name)
        logger.info("User removed the product from the wishlist.")
    except Exception as e:
        logger.error(f"Failed to remove product from wishlist: {e}")
        raise
