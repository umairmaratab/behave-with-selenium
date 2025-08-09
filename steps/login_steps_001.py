from behave import given, when, then
from pages.login_page_001 import LoginPage

@given("I am on the SauceDemo login page")
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.visit("https://www.saucedemo.com/")

@when('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@then("I should see the products page")
def step_impl(context):
    assert "inventory" in context.driver.current_url
