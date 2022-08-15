import pytest

from pages.DB_Page import DataBasePage

from configs.ui_parsing import new_username, new_password, first_name
from configs.ui_parsing import last_name, email, welcome_name
from configs.db_parser import *

import allure


class TestDB:

    db = DataBasePage()

    @allure.feature('Data base')
    @allure.story('Check name of created group in db appears on the site')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.data_base
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_check_group_name(self, db_conn, groups_page):
        with allure.step('Create new group in db'):
            self.db.executions(db_conn, create_group)
            with allure.step('Open groups page and refresh the page'):
                groups_page.refresh()
                with allure.step('Find created group name on the site'):
                    result = groups_page.name_of_created_group()
                    with allure.step('Check group name in db = name on site'):
                        assert result == group_name, \
                            f'Error: result is {result}'

    @allure.feature('Data base')
    @allure.story('Check info of created user on the site appears in db')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.data_base
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_check_user_in_db(self, db_conn, add_user_page):
        with allure.step('Create new user on the site'):
            add_user_page.user_creation(
                new_username,
                new_password,
                first_name,
                last_name,
                email
            )
            with allure.step('Get new user info from db'):
                result = self.db.user_info(db_conn, user_query)
                with allure.step('Check user info in db = filled user info'):
                    assert result == leila_info, f"Error: result is {result}"

    @allure.feature('Data base')
    @allure.story('Check created user joined created group in db')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.data_base
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_new_user_in_group(self, db_conn):
        with allure.step('Get info from db if user is in group'):
            result = self.db.check_user_in_group(
                db_conn,
                user_id,
                created_group_id,
                user_id_in_group,
                group_id_in_group
            )
            with allure.step('Check if user is in group'):
                assert result == user_in_group, f"Error: result is {result}"

    @allure.feature('Data base')
    @allure.story('Check created user can log in to the site')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.data_base
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_new_user_log_in(self, log_in_new_user, db_conn):
        with allure.step('Log in with new user and get welcome block name'):
            result = log_in_new_user.get_welcome_name_text()
            with allure.step('Check if welcome block name == user name'):
                assert result == welcome_name, f"Error: result is {result}"
