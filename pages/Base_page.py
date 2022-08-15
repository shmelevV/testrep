from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    main_url = "http://localhost:8000"

    def __init__(self, driver):
        self.driver = driver
        self.url = None

    def find_element(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(locator))

    def open_main_page(self):
        return self.driver.get(self.main_url)

    def open(self, url):
        return self.driver.get(url)

    def refresh(self):
        return self.driver.refresh()
