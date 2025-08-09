Feature: Product filtering

  @search
  Scenario: Filter products by price
    Given I am logged in to SauceDemo
    When I filter products by "Price (low to high)"
    Then products should be sorted accordingly
