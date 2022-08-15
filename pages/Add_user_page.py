from pages.Base_page import BasePage
from locators.Add_user_page_locators import AddUserPageLocators


class AddUserPage(BasePage, AddUserPageLocators):

    add_user_page = BasePage.main_url + '/admin/auth/user/add/'

    def open_add_user_page(self):
        self.open(self.add_user_page)

    def find_username_field(self):
        field = self.find_element(self.USERNAME)
        return field

    def fill_username_field(self, username):
        field = self.find_username_field()
        field.send_keys(username)
        return field

    def find_password_field(self):
        field = self.find_element(self.PASSWORD)
        return field

    def fill_password_field(self, password):
        field = self.find_password_field()
        field.send_keys(password)
        return field

    def find_confirm_passwd_field(self):
        field = self.find_element(self.CONFIRM_PASSWD)
        return field

    def fill_confirm_passwd_field(self, password):
        field = self.find_confirm_passwd_field()
        field.send_keys(password)
        return field

    def find_save_field(self):
        field = self.find_element(self.SAVE)
        return field

    def click_save_field(self):
        field = self.find_save_field()
        field.click()
        return field

    def find_firstname_field(self):
        field = self.find_element(self.FIRST_NAME)
        return field

    def fill_firstname_field(self, firstname):
        field = self.find_firstname_field()
        field.send_keys(firstname)
        return field

    def find_lastname_field(self):
        field = self.find_element(self.LAST_NAME)
        return field

    def fill_lastname_field(self, lastname):
        field = self.find_lastname_field()
        field.send_keys(lastname)
        return field

    def find_email_field(self):
        field = self.find_element(self.EMAIL)
        return field

    def fill_email_field(self, email):
        field = self.find_email_field()
        field.send_keys(email)
        return field

    def find_staff_field(self):
        field = self.find_element(self.SUPERUSER)
        return field

    def click_staff_field(self):
        field = self.find_staff_field()
        field.click()
        return field

    def add_to_group_field(self):
        field = self.find_element(self.ADD_TO_GROUP)
        return field

    def click_add_to_group_field(self):
        field = self.add_to_group_field()
        field.click()
        return field

    def user_creation(self, username, password, firstname, lastname, email):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.fill_confirm_passwd_field(password)
        self.click_save_field()
        self.fill_firstname_field(firstname)
        self.fill_lastname_field(lastname)
        self.fill_email_field(email)
        self.click_staff_field()
        self.click_add_to_group_field()
        self.click_save_field()
