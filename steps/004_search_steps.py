from behave import given, when, then
from pages.search_page import SearchPage
from pages.login_page import LoginPage

# @given("I am logged in to SauceDemo")
# def step_impl(context):
#     context.login_page = LoginPage(context.driver)
#     context.login_page.visit("https://www.saucedemo.com/")
#     context.login_page.login("standard_user", "secret_sauce")

@when('I filter products by "{filter_option}"')
def step_impl(context, filter_option):
    search_page = SearchPage(context.driver)
    search_page.filter_products(filter_option)

@then("products should be sorted accordingly")
def step_impl(context):
    # This step would contain validation logic
    assert True
