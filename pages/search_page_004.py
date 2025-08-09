from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    PRODUCT_LIST = (By.CLASS_NAME, "inventory_item")
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def filter_products(self, filter_option):
        dropdown = self.find(self.FILTER_DROPDOWN)
        dropdown.click()
        dropdown.find_element(By.XPATH, f"//option[text()='{filter_option}']").click()

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_LIST))
