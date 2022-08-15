import configparser


config = configparser.ConfigParser()
config.read('configs/ui_config.ini')

# admin login info
username = config.get("login_info", "username")
password = config.get("login_info", "password")

# new user login info
new_username = config.get("new_user_info", "username")
new_password = config.get("new_user_info", "password")
first_name = config.get("new_user_info", "first_name")
last_name = config.get("new_user_info", "last_name")
email = config.get("new_user_info", "email")

# new date and time for picture
data = config.get("picture_info", "data")
time = config.get("picture_info", "time")
new_date = config.get("picture_info", "new_date")

# false admin button texts
false_1 = config.get("button_false", "text1")
false_2 = config.get("button_false", "text2")
false_3 = config.get("button_false", "text3")

# welcome name of new user
welcome_name = config.get("welcome", "welcome_name")

# value for select to choose
select_by_value = config.get("select", "select_by_value")
