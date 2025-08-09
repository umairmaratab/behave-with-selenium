from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.cart_page_002 import CartPage
from pages.checkout_page_003 import CheckoutPage
from pages.login_page_001 import LoginPage

@given("I have a product in the cart")
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.visit("https://www.saucedemo.com/")
    context.login_page.login("standard_user", "secret_sauce")
    context.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

@when('I proceed to checkout with "{first_name}" "{last_name}" "{postal_code}"')
def step_impl(context, first_name, last_name, postal_code):
    cart_page = CartPage(context.driver)
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(context.driver)
    checkout_page.fill_checkout_info(first_name, last_name, postal_code)
    checkout_page.finish_checkout()

@then("I should see the checkout complete page")
def step_impl(context):
    assert "checkout-complete" in context.driver.current_url
