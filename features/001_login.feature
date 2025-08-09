Feature: Login functionality for SauceDemo

  @saucedemo
  Scenario: Valid user can login
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should see the products page
