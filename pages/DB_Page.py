import psycopg2
from psycopg2 import Error
from configs.db_parser import user, password, host, database, group_name
from configs.ui_parsing import new_username


class DataBasePage:

    def __init__(self):
        self.conn = None

    def create_connection(self):

        my_connection = None

        try:
            my_connection = psycopg2.connect(
                user=user,
                password=password,
                host=host,
                database=database
            )
        except Error as e:
            print(f"The error {e} occurred")
        return my_connection

    def executions(self, connection, query):
        self.conn = connection
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            self.conn.commit()

    def selections(self, connection, query):
        self.conn = connection
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def user_info(self, connection, query):
        result = self.selections(connection, query)
        db_first_name = ''
        db_last_name = ''
        db_email = ''
        for el in result:
            db_first_name += el[0]
            db_last_name += el[1]
            db_email += el[2]
        return f'{db_first_name}, {db_last_name}, {db_email}'

    def user_and_group_id(self, conn, us_id, gr_id):
        id_user = self.selections(conn, us_id)
        id_group = self.selections(conn, gr_id)
        return id_user + id_group

    def user_and_group_id_in_group(self, conn, us_id_gr, gr_id_gr):
        id_user_group = self.selections(conn, us_id_gr)
        id_group_group = self.selections(conn, gr_id_gr)
        return id_user_group + id_group_group

    def check_user_in_group(self, conn, us_id, gr_id, us_id_gr, gr_id_gr):
        user_group_id = self.user_and_group_id(conn, us_id, gr_id)
        user_group_id_in_group = self.user_and_group_id_in_group(
            conn,
            us_id_gr,
            gr_id_gr
        )
        if user_group_id == user_group_id_in_group:
            return f'{new_username} is in the group {group_name}'
        else:
            return f'{user_group_id} is not {user_group_id_in_group}'
