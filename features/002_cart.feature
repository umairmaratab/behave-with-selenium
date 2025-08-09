Feature: Cart functionality

  @cart
  Scenario: Add product to cart and verify
    Given I am logged in to SauceDemo
    When I add a product to the cart
    Then the cart should have 1 item
