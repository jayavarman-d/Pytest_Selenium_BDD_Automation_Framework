import pytest
import allure
from pytest_bdd import given, then, when, scenario, parsers
from tests.conftest import *
from utils.PageFactory import ObjectPage
from utils.Loggers import setup_logger

logger = setup_logger(__name__, 'test_signin.log')


@pytest.mark.signin
@pytest.mark.regression
@allure.feature('Login Functionality')
@pytest.mark.usefixtures('browser_setup')
@pytest.mark.usefixtures('object_return')
@scenario(login_feature, "Login Invalid (credential mismatch)")
@allure.story('Login Invalid (credential mismatch)')
@allure.title('Validating with Invalid Credentials')
def test_invalid_sign():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during invalid sign-in: {e}")
        pytest.fail(f"Test failed during invalid sign-in: {e}")


@given('User is on the login page')
@allure.step('Given User is on Login Page')
def given_user_on_signin_page(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_path()
        logger.info("User navigated to the signin page.")
    except Exception as e:
        logger.error(f"Failed to navigate to the signin page: {e}")
        raise


@when(parsers.parse('User enters invalid Username {username}'))
@allure.step('When User enters invalid Username')
def when_user_enters_the_invalid_username(browser_setup, object_return, username):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_field_username(username)
        logger.info("User entered invalid username.")
    except Exception as e:
        logger.error(f"Failed to enter invalid username: {e}")
        raise


@when(parsers.parse('User enters invalid Password {password}'))
@allure.step('And User enters invalid Password')
def and_user_enters_the_invalid_password(browser_setup, object_return, password):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_field_password(password)
        logger.info("User entered invalid password.")
    except Exception as e:
        logger.error(f"Failed to enter invalid password: {e}")
        raise


@when('User Clicks signin button')
@allure.step('When User Clicks signin button')
def when_user_clicks_signin_button(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_button()
        # test_name = os.path.basename(__file__)
        fail_text = page_obj.signin_fail_text()
        assert fail_text == "Error: Incorrect login or password provided."
        logger.info("User clicked the signin button.")
    except Exception as e:
        logger.error(f"Failed to click signin button: {e}")
        raise


@pytest.mark.signin
@pytest.mark.regression
@allure.story('Valid Login')
@allure.title('Validating with valid Credentials')
@scenario(login_feature, "Valid Login")
@pytest.mark.usefixtures('browser_setup')
def test_valid_sign():
    try:
        pass
    except Exception as e:
        logger.error(f"Test failed during valid sign-in: {e}")
        pytest.fail(f"Test failed during valid sign-in: {e}")


@given('User is on the login page')
@allure.step('Given User is on Login Page')
def given_user_on_signin_page(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_path()
        logger.info("User navigated to the signin page.")
    except Exception as e:
        logger.error(f"Failed to navigate to the signin page: {e}")
        raise


@when(parsers.parse('User enters valid Username'))
@allure.step('When User enters valid Username')
def when_user_enters_the_valid_username(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_field_valid_username()
        logger.info(f"User entered valid username:")
    except Exception as e:
        logger.error(f"Failed to enter valid username: {e}")
        raise


@when(parsers.parse('User enters valid Password'))
@allure.step('And User enters valid Password')
def and_user_enters_the_valid_password(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_field_valid_password()
        logger.info(f"User entered valid password:")
    except Exception as e:
        logger.error(f"Failed to enter valid password: {e}")
        raise


@when('User Clicks signin button')
@allure.step('When User Clicks signin button')
def when_user_clicks_signin_button(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        page_obj.signin_button()
        logger.info("User clicked the signin button.")
    except Exception as e:
        logger.error(f"Failed to click signin button: {e}")
        raise


@then('Page will be redirected to customer Account page')
@allure.step('Then the page will be redirected to customer Account page')
def then_user_logged_in(browser_setup, object_return):
    try:
        page_obj = object_return.home_page(browser_setup)
        text = page_obj.signin_pass_text()
        assert text == 'MY ACCOUNT'
        logger.info("User logged in Successfully.")
    except Exception as e:
        logger.error(f"Failed to verify account page: {e}")
        raise
