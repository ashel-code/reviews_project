from mysql.connector import connect


class DatabaseActions:
    @staticmethod
    def get_all():
        with connect(
            host="localhost",
            user="root",
            password="BackupDR",
            database="reviews"
        ) as connection:
            query = 'SELECT * FROM reviews'
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
                cursor.close()
            connection.close()
