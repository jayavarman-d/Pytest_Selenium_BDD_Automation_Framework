import pytest
import allure
from tests.conftest import *
from utils.PageFactory import ObjectPage
from pytest_bdd import given, when, then, scenario
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'test_filter.log')


@pytest.mark.regression
@allure.feature('Filter Functionality')
@pytest.mark.usefixtures('browser_setup')
@pytest.mark.usefixtures('object_return')
@scenario(search_filter_feature, "Checking Filters in the Conditioner Page")
@allure.story('Checking Filters in the Conditioner Page')
@allure.title('Validating Filters is Working Properly')
def test_filter():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during filter functionality: {e}")
        pytest.fail(f"Test failed during filter functionality: {e}")


@given('the user is on the Conditioner Page')
@allure.step('Given the user is on the Conditioner Page')
def given_the_user_on_conditioner_page(browser_setup, object_return):
    try:
        page_obj = object_return.product_catalog_page(browser_setup)
        page_obj.navbar_selection()
        logger.info("User navigated to the conditioner page.")
    except Exception as e:
        logger.error(f"Failed to navigate to the conditioner page: {e}")
        raise


@when('User clicks on the sort by Name A-Z')
@allure.step('When User clicks on the sort by Name A-Z')
def when_user_clicks_asc(browser_setup, object_return):
    try:
        page_obj = object_return.product_catalog_page(browser_setup)
        prod_asc = page_obj.sort_asc()
        assert prod_asc == sorted(prod_asc)
        logger.info("User clicked on the sort by Name A-Z.")
    except Exception as e:
        logger.error(f"Failed to sort by Name A-Z: {e}")
        raise


@when('User clicks on the sort by Name Z-A')
@allure.step('And User clicks on the sort by Name Z-A')
def and_user_clicks_desc(browser_setup, object_return):
    try:
        page_obj = object_return.product_catalog_page(browser_setup)
        prod_desc = page_obj.sort_desc()
        assert prod_desc == sorted(prod_desc, reverse=True)
        logger.info("User clicked on the sort by Name Z-A.")
    except Exception as e:
        logger.error(f"Failed to sort by Name Z-A: {e}")
        raise


@when('User clicks on the sort by Price Low > High')
@allure.step('When User clicks on the sort by Price Low > High')
def when_user_clicks_price_asc(browser_setup, object_return):
    try:
        page_obj = object_return.product_catalog_page(browser_setup)
        price_asc = page_obj.sort_price_asc()
        assert price_asc == sorted(price_asc)
        logger.info("User clicked on the sort by Price Low > High.")
    except Exception as e:
        logger.error(f"Failed to sort by Price Low > High: {e}")
        raise


@when('User clicks on the sort by Price High > Low')
@allure.step('And User clicks on the sort by Price High > Low')
def and_user_clicks_price_desc(browser_setup, object_return):
    try:
        page_obj = object_return.product_catalog_page(browser_setup)
        price_desc = page_obj.sort_price_desc()
        assert price_desc == sorted(price_desc)
        logger.info("User clicked on the sort by Price High > Low.")
    except Exception as e:
        logger.error(f"Failed to sort by Price High > Low: {e}")
        raise


@when('User clicks on the sort by Rating Highest')
@allure.step('When User clicks on the sort by Rating Highest')
def when_user_clicks_rating_high(browser_setup, object_return):
    try:
        page_obj = object_return.product_catalog_page(browser_setup)
        rat_high = page_obj.sort_rating_high()
        assert rat_high == sorted(rat_high, reverse=True)
        logger.info("User clicked on the sort by Rating Highest.")
    except Exception as e:
        logger.error(f"Failed to sort by Rating Highest: {e}")
        raise


@when('User clicks on the sort by Rating Lowest')
@allure.step('And User clicks on the sort by Rating Lowest')
def and_user_clicks_rating_low(browser_setup, object_return):
    try:
        page_obj = object_return.product_catalog_page(browser_setup)
        rat_low = page_obj.sort_rating_low()
        assert rat_low == sorted(rat_low)
        logger.info("User clicked on the sort by Rating Lowest.")
    except Exception as e:
        logger.error(f"Failed to sort by Rating Lowest: {e}")
        raise


@when('User clicks on the sort by Date New>Old')
@allure.step('And User clicks on the sort by Date New>Old')
def when_user_clicks_date_desc(browser_setup, object_return):
    try:
        page_obj = object_return.product_catalog_page(browser_setup)
        date_desc = page_obj.sort_date_new_old()
        assert date_desc == sorted(date_desc, reverse=True)
        logger.info("User clicked on the sort by Date New > Old.")
    except Exception as e:
        logger.error(f"Failed to sort by Date New > Old: {e}")
        raise


@when('User clicks on the sort by Date Old>New')
@allure.step('And User clicks on the sort by Date Old>New')
def and_user_clicks_date_asc(browser_setup, object_return):
    try:
        page_obj = object_return.product_catalog_page(browser_setup)
        date_asc = page_obj.sort_date_old_new()
        assert date_asc == sorted(date_asc)
        logger.info("User clicked on the sort by Date Old > New.")
    except Exception as e:
        logger.error(f"Failed to sort by Date Old > New: {e}")
        raise


@then('User can edit any Filters')
@allure.step('Then User can edit any filters')
def then_user_can_edit_any_filter():
    pass
