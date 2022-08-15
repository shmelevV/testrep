from pages.Base_page import BasePage
from locators.Main_page_locators import MainPageLocators


class MainPage(BasePage, MainPageLocators):

    def main_page(self):
        self.open_main_page()

    def find_all_pictures_data(self):
        pictures_data = self.find_elements(self.PICTURES_DATA)
        data_text = [el.text for el in pictures_data]
        return data_text

    def find_admin_button_field(self):
        field = self.find_element(self.GO_TO_ADMIN)
        return field

    def get_text_admin_button(self):
        field = self.find_admin_button_field()
        return field.text
