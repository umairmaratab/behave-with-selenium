import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

REPORTS_DIR = os.path.join(os.getcwd(), "reports")
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

def before_all(context):
    browser_mode = context.config.userdata.get("browser", "headless")
    options = webdriver.ChromeOptions()

    if browser_mode == "headless":
        options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if scenario.status.name == "failed":
        safe_name = scenario.name.replace(" ", "_")
        screenshot = os.path.join(REPORTS_DIR, f"{safe_name}.png")
        context.driver.save_screenshot(screenshot)


def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()
