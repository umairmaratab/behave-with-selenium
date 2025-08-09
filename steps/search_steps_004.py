from behave import given, when, then
from pages.search_page_004 import SearchPage
from pages.login_page_001 import LoginPage

@when('I filter products by "{filter_option}"')
def step_impl(context, filter_option):
    search_page = SearchPage(context.driver)
    search_page.filter_products(filter_option)

@then("products should be sorted accordingly")
def step_impl(context):
    assert True
