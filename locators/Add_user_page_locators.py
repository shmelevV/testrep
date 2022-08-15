from selenium.webdriver.common.by import By


class AddUserPageLocators:

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password1")
    CONFIRM_PASSWD = (By.NAME, "password2")
    SAVE = (By.CLASS_NAME, "default")
    FIRST_NAME = (By.ID, "id_first_name")
    LAST_NAME = (By.ID, "id_last_name")
    EMAIL = (By.ID, "id_email")
    LOG_OUT = (By.XPATH, "//*[@id='user-tools']/a[3]")
    SUPERUSER = (By.ID, "id_is_staff")
    ADD_TO_GROUP = (By.ID, "id_groups_add_all_link")
