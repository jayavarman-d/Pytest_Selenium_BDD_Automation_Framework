Feature: Full Purchase Flow

Scenario: Full Flow from Login to Buying a product
  Given User is on Homepage
  When User clicks sign in
  And User should enter the credentials for login
  When User successfully signed in and go to home
  And Navigate to Skincare
  When User selects the Product
  And Add the product to the cart
  When Confirming the checkout
  And User Confirm Order
  Then the message "Your order has been Processed"
