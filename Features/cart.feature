Feature: Cart Functionality

  Scenario: Checking the requested Quantity is not available
    Given The User is on the Homepage
    When User navigate to Skincare in Navbar and select Gift Ideas & Sets
    And User Selects Night Care Crema Nera Obsidian Mineral Complex
    When The User enters the quantity > availability into the quantity field
    And User clicks on the Add to Cart Button
    Then User should not be able to checkout due to quantity higher than availability

  Scenario: Remove items from the cart
    Given User Is on the Homepage
    When User clicks on signin and signin using Credentials
    And User moves to the Homepage
    When the user clicks the cart page
    And starts to remove products from the cart


  Scenario: The User should be able to buy a product without being logged in but the details should be collected
    Given User is on Homepage
    When User moves to Navbar
    And User selects the Product
    When User adds the Product to Cart
    And User selects Guest Account
    When User enters required details for the shipping (mail,name,company,street,city)
    And User enters into the payment method and Checkout


  Scenario: Download Invoice and check it
    Given User is on Homepage
    When User clicks on signin
    And User signin using Credentials
    When User Clicks on Order History
    And User clicks on view
    When User clicks on Print
    And User Clicks save in print Dialog

