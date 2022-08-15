import configparser


config = configparser.ConfigParser()
config.read('configs/api_config.ini')

# requests user
create_user = config.get("requests_user", "create")
log_in = config.get("requests_user", "log_in")
get_user_info = config.get("requests_user", "get_user_info")
log_out = config.get("requests_user", "log_out")
delete_user = config.get("requests_user", "delete")

# user
user_info = config.get("user", "info")

# requests pet
create_pet = config.get("requests_pet", "create")
find_pet = config.get("requests_pet", "find")
update_pet = config.get("requests_pet", "update")

# pet
pet_info = config.get("pet", "info")
new_pet_name = config.get("pet", "new_name")
