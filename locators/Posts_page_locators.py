from selenium.webdriver.common.by import By


class PostsPageLocators:

    CHECKBOXES = (By.XPATH, "/html/body/div/div[3]/div/div[1]/div/div/div/form/div[2]/table/tbody/tr[1]/td/input")
    SELECT = (By.TAG_NAME, "select")
    GO = (By.CLASS_NAME, "button")
    SURE = (By.CSS_SELECTOR, "[type='submit']")
    ALL_PICS = (By.PARTIAL_LINK_TEXT, "Post object")
    DATE = (By.CLASS_NAME, "vDateField")
    TIME = (By.CLASS_NAME, "vTimeField")
    SAVE = (By.CSS_SELECTOR, "[type='submit']")
