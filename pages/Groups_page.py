from pages.Base_page import BasePage
from locators.Groups_page_locators import GroupsPageLocators


class GroupsPage(BasePage, GroupsPageLocators):

    groups_url = BasePage.main_url + '/admin/auth/group/'

    def open_groups_page(self):
        self.open(self.groups_url)

    def name_of_created_group(self):
        my_group = self.find_element(self.MY_GROUP)
        return my_group.text
