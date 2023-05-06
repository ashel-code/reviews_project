from mysql.connector import connect
from structure.unvectorized_data import Unvectorized


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
                cursor.close()
            connection.close()
        return result

    @staticmethod
    def get_unvectorized():
        with connect(
                host="localhost",
                user="root",
                password="BackupDR",
                database="reviews"
        ) as connection:
            query = 'SELECT id, review_text FROM reviews WHERE vector IS NULL'
            with connection.cursor() as cursor:
                cursor.execute(query)
                pre_result = cursor.fetchall()
                cursor.close()
            connection.close()
        print(pre_result)
        result = DatabaseActions.convert_to_unvectorized_class(pre_result)
        return result

    @staticmethod
    def convert_to_unvectorized_class(data):
        result = []
        for d in data:
            temp = Unvectorized(d[0], d[1])
            result.append(temp)
        return result
