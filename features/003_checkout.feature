Feature: Checkout process

  @checkout
  Scenario: Complete a checkout
    Given I have a product in the cart
    When I proceed to checkout with "John" "Doe" "12345"
    Then I should see the checkout complete page
