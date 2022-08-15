from pages.Base_page import BasePage
from locators.User_page_locators import UserPageLocators


class UserPage(BasePage, UserPageLocators):

    user_page = BasePage.main_url + '/admin/auth/user/'

    def open_user_page(self):
        self.open(self.user_page)

    def find_logout_field(self):
        field = self.find_element(self.LOG_OUT)
        return field

    def click_logout_field(self):
        field = self.find_logout_field()
        field.click()
        return field
