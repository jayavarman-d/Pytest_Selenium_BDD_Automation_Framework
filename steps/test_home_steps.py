import allure
from tests.conftest import *
from pytest_bdd import given, then, when, scenario
from utils.PageFactory import ObjectPage
from utils.Loggers import setup_logger


logger = setup_logger(__name__, 'test_home_steps.log')


@pytest.mark.home
@pytest.mark.regression
@allure.feature('Navbar and Homepage Navigation and Search Functionality')
@pytest.mark.usefixtures('browser_setup')
@pytest.mark.usefixtures('object_return')
@scenario(Navigation_feature, "Validating the Navbar is working Properly")
@allure.story('Validating the Navbar is working Properly')
@allure.title('Validating Navbar is Working')
def test_navbar():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during navbar functionality: {e}")
        pytest.fail(f"Test failed during navbar functionality: {e}")


@given('User is on the homepage')
@allure.step('Given User is on the homepage')
def given_user_is_on_homepage(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User is on the homepage.")
    except Exception as e:
        logger.error(f"Failed to navigate to homepage: {e}")
        raise


@when('User Navigates to Apparel & Accessories')
@allure.step('When User Navigates to Apparel & Accessories')
def when_user_clicks_navbar(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.navbar()
        logger.info("User navigated to the Navbar.")
    except Exception as e:
        logger.error(f"Failed to click on navbar: {e}")
        raise


@when('User Clicks on T-Shirts in the Hover')
@allure.step('And User Clicks on T-Shirts in the Hover')
def and_user_clicks_on_tshirt(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.navbar_select()
        assert page_obj.navbar_assert() == 'T-SHIRTS'
        logger.info("User clicked on T-Shirts in the hover menu.")
    except Exception as e:
        logger.error(f"Failed to click on T-Shirts: {e}")
        raise


@pytest.mark.home
@pytest.mark.regression
@scenario(Navigation_feature, "Checking Whether the search bar is working or not")
@allure.story('Checking Whether the search bar is working or not')
@allure.title('Validating Searchbar Functionality')
def test_search_product():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during search functionality: {e}")
        pytest.fail(f"Test failed during search functionality: {e}")


@given('The User is on the home page')
@allure.step('Given the User is on the home page')
def given_user_on_homepage(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.home_path()
        logger.info("User is on the homepage for search.")
    except Exception as e:
        logger.error(f"Failed to navigate to homepage for search: {e}")
        raise


@when('User Clicks on the Searchbar')
@allure.step('When User clicks on the Searchbar')
def when_user_clicks_on_search(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.searchbar()
        logger.info("User clicked on the search bar.")
    except Exception as e:
        logger.error(f"Failed to click on search bar: {e}")
        raise


@when('User Clicks on the Search Button')
@allure.step('And User clicks on Search button')
def and_user_clicks_on_search_button(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.search_product()
        assert "T-Shirt" in page_obj.search_assert()
        logger.info("User clicked on the search button.")
    except Exception as e:
        logger.error(f"Failed to click on search button: {e}")
        raise
