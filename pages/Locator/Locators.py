from selenium.webdriver.common.by import By


class Locators:

    # Signin Page
    signin_page = (By.XPATH, "//li[@data-id='menu_account']//span[@class='menu_text' and text()='Account']")
    signin_page_login_id = (By.XPATH, "//input[@name='loginname']")
    signin_page_password = (By.XPATH, "//input[@name='password']")
    signin_page_button = (By.XPATH, "//button[@type='submit' and @title = 'Login']")
    signin_failed_text = (By.XPATH, "//div[@class='alert alert-error alert-danger']")
    signin_pass_text = (By.XPATH, "//span[@class='maintext']")

    # Home Page
    home_path = (By.XPATH, "//img[@title='Automation Test Store']")

    home_navbar_hover = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=product/category&path=68']")
    home_navbar_hover_dropdown = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=product/category&path=68_70']")
    home_navbar_category = (By.XPATH, "//span[@class = 'maintext']")
    home_search_bar = (By.XPATH, "//input[@id='filter_keyword']")
    home_search_bar_icon = (By.XPATH, "//div[@class='button-in-search']")
    home_search_assert = (By.XPATH, "//span[@class = 'bgnone']")

    # Product Catalog Filter
    product_catalog_navbar = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=product/category&path=52']")
    product_catalog_navbar_dropdown = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=product/category&path=52_54']")
    product_catalog_product_sort = (By.XPATH, "//select[@name='sort']")
    product_catalog_product_sort_asc = (By.XPATH, "//select[@name='sort']//option[@value='pd.name-ASC']")
    product_catalog_product_sort_desc = (By.XPATH, "//select[@name='sort']//option[@value='pd.name-DESC']")
    product_catalog_product_sort_price_asc = (By.XPATH, "//select[@name='sort']//option[@value='p.price-ASC']")
    product_catalog_product_sort_price_desc = (By.XPATH, "//select[@name='sort']//option[@value='p.price-DESC']")
    product_catalog_product_sort_rating_high = (By.XPATH, "//select[@name='sort']//option[@value='rating-DESC']")
    product_catalog_product_sort_rating_low = (By.XPATH, "//select[@name='sort']//option[@value='rating-ASC']")
    product_catalog_product_sort_date_old_new = (By.XPATH, "//select[@name='sort']//option[@value='date_modified-ASC']")
    product_catalog_product_sort_date_new_old = (By.XPATH, "//select[@name='sort']//option[@value='date_modified-DESC']")
    product_catalog_product_price = (By.XPATH, "//div[@class='pricetag jumbotron']//div[@class = 'oneprice']")
    product_catalog_product_list = (By.XPATH, "//div[@class = 'fixed']//a[@class = 'prdocutname']")

    # Product Page
    product_quantity_nav_skincare = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=product/category&path=43']")
    product_quantity_nav_hover_dropdown = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=product/category&path=43_45']")
    product_quantity_select = (By.XPATH, "//a[@class='prdocutname' and @title ='Night Care Crema Nera Obsidian Mineral Complex']")
    product_quantity_getter = (By.XPATH, "//ul[@class='productinfo']//span[@class='productinfoleft']/parent::li")
    product_quantity_field = (By.XPATH, "//input[@type='text' and @name ='quantity']")
    product_quantity_add_to_cart = (By.XPATH, "//a[@href='#' and @class ='cart']")
    product_quantity_checkout = (By.XPATH, "//a[@class='btn btn-orange pull-right' and @id ='cart_checkout1']")
    # product_quantity_cart_message = (By.XPATH, "//div[@class='alert alert-error alert-danger']")
    product_quantity_checkout_confirm = (By.XPATH, "//button[@title = 'Confirm Order']")
    product_quantity_checkout_confirm_message = (By.XPATH, "//div[@class='alert alert-error alert-danger']/strong")

    # Wishlist Page
    wishlist_product = (By.XPATH, "//a[@title='ck one shock for him Deodorant']")
    wishlist_product_button = (By.XPATH, "//i[@class='fa fa-plus-square fa-fw']")
    wishlist_product_profile_hover = (By.XPATH, "//div[@class='menu_text']")
    wishlist_product_profile_hover_dropdown = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=account/wishlist']")
    wishlist_product_remove = (By.XPATH, "//i[@class='fa fa-trash-o fa-fw']")

    # Remove Cart
    remove_cart_hover = (By.XPATH, "//ul[@class='nav topcart pull-left']//i[@class='fa fa-shopping-cart fa-fw']")
    remove_cart_hover_button = (By.XPATH, "//ul[@class='nav topcart pull-left']//a[@class='btn btn-default']")
    remove_cart_item = (By.XPATH, "//a[@class='btn btn-sm btn-default']")
    remove_cart_list_item = (By.XPATH, "//td[@class='align_left']//a[contains(text(),'')]")


    # Buy Without Login
    buy_without_login_add_cart = (By.XPATH, "//i[@class='fa fa-cart-plus fa-fw']")
    buy_without_login_checkout = (By.XPATH, "//a[@id = 'cart_checkout1']//i[@class='fa fa-shopping-cart fa-fw']")
    buy_without_login_guest = (By.XPATH, "//input[@id = 'accountFrm_accountguest']")
    buy_without_login_guest_button = (By.XPATH, "//button[@title = 'Continue']")

    # bo_input_path = (By.XPATH, f"//input[@name = 'xxxx']")

    def wo_login_paths(self, path):
        return (By.XPATH, f"//input[@name = '{path}']")

    def wo_login_paths_select(self, path):
        return (By.XPATH, f"//select[@name='{path}']")

    # buy_without_login_guest_firstname = (By.XPATH, "//input[@name = 'firstname']")
    # buy_without_login_guest_lastname = (By.XPATH, "//input[@name = 'lastname']")
    # buy_without_login_guest_mail = (By.XPATH, "//input[@name = 'email' and @id='guestFrm_email']")
    # buy_without_login_guest_mobile = (By.XPATH, "//input[@name = 'telephone']")
    # buy_without_login_guest_fax = (By.XPATH, "//input[@name = 'fax']")
    # buy_without_login_guest_company = (By.XPATH, "//input[@name = 'company']")
    # buy_without_login_guest_address1 = (By.XPATH, "//input[@name = 'address_1']")
    # buy_without_login_guest_address2 = (By.XPATH, "//input[@name = 'address_2']")
    # buy_without_login_guest_city = (By.XPATH, "//input[@name = 'city']")
    # buy_without_login_guest_state = (By.XPATH, "//select[@name = 'zone_id']//option[text() ='Paris / Ill de France']")
    # buy_without_login_guest_country = (By.XPATH, "//select[@name = 'country_id']//option[text() ='France']")
    # buy_without_login_guest_postcode = (By.XPATH, "//input[@name = 'postcode']")
    buy_without_login_guest_checkbox = (By.XPATH, "//input[@name = 'shipping_indicator']")
    buy_without_login_guest_confirm = (By.XPATH, "//button[@title = 'Continue']")
    buy_without_login_guest_amount = (By.XPATH, "//span[@class='bold totalamout']")
    buy_without_login_guest_confirm_checkout = (By.XPATH, "//button[@title = 'Confirm Order']")
    buy_without_login_guest_confirm_message = (By.XPATH, "//span[contains(.,'Your Order Has Been Processed!')]")

    # Download Invoice
    download_invoice_order_history = (By.XPATH, "//a[@data-original-title = 'Order history']")
    download_invoice_view = (By.XPATH, "//i[@class = 'fa fa-info']")
    download_invoice_print = (By.XPATH, "//a[@title = 'Print']")

    # Product Page
    product_page_product = (By.XPATH, "//a[@title='Casual 3/4 Sleeve Baseball T-Shirt']")
    product_page_size = (By.XPATH, "//select[@name='option[353]']")

    # Final Order Confirmation
    order_confirm_message = (By.XPATH, "//span[@class='maintext']")
