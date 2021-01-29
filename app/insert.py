from database import Mysql

mysql = Mysql()

with mysql.connection:
    with mysql.connection.cursor() as cursor:
        sql = "INSERT INTO `chart_data` (`x`, `y`) VALUES (%s, %s)"
        cursor.execute(sql, (1, 1))

        sql = "INSERT INTO `chart_data` (`x`, `y`) VALUES (%s, %s)"
        cursor.execute(sql, (2, 2))

        sql = "INSERT INTO `chart_data` (`x`, `y`) VALUES (%s, %s)"
        cursor.execute(sql, (3, 3))

        mysql.connection.commit()

print("Finished!")
