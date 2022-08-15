from selenium.webdriver.support.select import Select

from pages.Base_page import BasePage
from locators.Posts_page_locators import PostsPageLocators
from configs.ui_parsing import select_by_value


class PostsPage(BasePage, PostsPageLocators):

    posts_url = BasePage.main_url + '/admin/app/post/'

    def open_posts_page(self):
        self.open(self.posts_url)

    def find_first_pic_field(self):
        field = self.find_elements(self.ALL_PICS)
        return field[-1]

    def click_first_pic_field(self):
        field = self.find_first_pic_field()
        field.click()
        return field

    def find_date_field(self):
        field = self.find_element(self.DATE)
        return field

    def find_time_field(self):
        field = self.find_element(self.TIME)
        return field

    def set_new_date(self, date):
        field = self.find_date_field()
        field.clear()
        field.send_keys(date)
        return field

    def set_new_time(self, time):
        field = self.find_time_field()
        field.clear()
        field.send_keys(time)
        return field

    def find_save_field(self):
        field = self.find_element(self.SAVE)
        return field

    def click_save_field(self):
        field = self.find_save_field()
        field.click()
        return field

    def find_checkbox_first_pic_field(self):
        checkboxes = self.find_elements(self.CHECKBOXES)
        return checkboxes[-1]

    def click_checkbox_first_pic_field(self):
        field = self.find_checkbox_first_pic_field()
        field.click()
        return field

    def select_delete_all(self):
        select = Select(self.find_element(self.SELECT))
        result = select.select_by_value(select_by_value)
        return result

    def find_go_field(self):
        field = self.find_element(self.GO)
        return field

    def click_go_field(self):
        field = self.find_go_field()
        field.click()
        return field

    def find_sure_field(self):
        field = self.find_element(self.SURE)
        return field

    def click_sure_field(self):
        field = self.find_sure_field()
        field.click()
        return field

    def set_new_date_and_time(self, data, time):
        self.click_first_pic_field()
        self.set_new_date(data)
        self.set_new_time(time)
        self.click_save_field()

    def delete_first_pic(self):
        self.click_checkbox_first_pic_field()
        self.select_delete_all()
        self.click_go_field()
        self.click_sure_field()
