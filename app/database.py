import pymysql.cursors


class Mysql:
    def __init__(self):
        self.connection = pymysql.connect(
            host="db",
            user="root",
            password="admin",
            database="mysql_db",
            cursorclass=pymysql.cursors.DictCursor,
        )
