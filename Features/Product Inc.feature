Feature: Product Interaction

  Scenario: Checking add to Wishlist and remove is working or not
    Given User is on the homepage
      When User clicks on login and move to login page
      And User logs using username and password
      When User moves to Homepage
      And The user is on a product page and select it
      When Added a product to wishlist
      And User Go to Profile
      When User selects wishlist
      And User was able to view the products which were added and removes it


  Scenario: Product Selection Bug
    Given The User is on the Homepage
	When User navigates to Navbar and User selects the T-shirt Category
	And User select the Baseball T-shirt
    When User selects the model
	And User clicks the add to cart

#  Scenario: Checking the tile description of the products
#    Given the user is on the homepage
#    When the user searches for the product
#    And the user select the option for product description
#    Then the user can preview product description before selecting a product

#  Scenario: Checking the call to order option in the products page
#    Given the user is on the homepage
#    When user click on Makeup in Navbar
#    And user selects L'EXTRÊME Instant Extensions Lengthening
#    When user clicks call to order option
#    And user is navigated to contact us form
#    Then After user filled the form "Your enquiry has been successfully sent to the store owner!" should be shown
