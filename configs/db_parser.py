import configparser


config = configparser.ConfigParser()
config.read('configs/db_config.ini')

# connection
user = config.get("connection", "user")
password = config.get("connection", "password")
host = config.get("connection", "host")
database = config.get("connection", "database")

# queries
create_group = config.get("queries", "create")
delete_group = config.get("queries", "delete_group")
delete_user = config.get("queries", "delete_user")
delete_auth_user_group = config.get("queries", "delete_auth_user_group")
user_query = config.get("queries", "user")
user_id = config.get("queries", "user_id")
created_group_id = config.get("queries", "created_group_id")
user_id_in_group = config.get("queries", "user_id_in_group")
group_id_in_group = config.get("queries", "group_id_in_group")

# created_group
group_name = config.get("created_group", "group_name")

# created user
leila_info = config.get("created_user", "leila_info")
user_in_group = config.get("created_user", "user_in_group")
