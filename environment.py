from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    browser_mode = context.config.userdata.get("browser", "headless")
    options = webdriver.ChromeOptions()

    if browser_mode == "headless":
        options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(10)

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()
