from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.cart_page import CartPage

@given("I am logged in to SauceDemo")
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.visit("https://www.saucedemo.com/")
    context.login_page.login("standard_user", "secret_sauce")

@when("I add a product to the cart")
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

@then("the cart should have 1 item")
def step_impl(context):
    cart_page = CartPage(context.driver)
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert cart_page.get_cart_items_count() == 1
