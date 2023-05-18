from mysql.connector import connect
from structure.unvectorized_data import Unvectorized
from get_config import data

class DatabaseActions:
    db_config = {
        "host": data('db_host'),
        "user": data('db_user'),
        "password": data('db_password'),
        "database": data('db_database'),
    }

    connection = connect(**db_config)

    @staticmethod
    def get_all():
        query = 'SELECT * FROM reviews'
        with DatabaseActions.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
        DatabaseActions.connection.close()
        return result

    @staticmethod
    def get_unvectorized():
        query = 'SELECT id, review_text FROM reviews WHERE vector IS NULL'
        with DatabaseActions.connection.cursor() as cursor:
            cursor.execute(query)
            pre_result = cursor.fetchall()
            cursor.close()
        DatabaseActions.connection.close()
        result = DatabaseActions.convert_to_unvectorized_class(pre_result)
        return result

    @staticmethod
    def add_element(rating, review_date, author, review_text, restaurant):
        query = f'INSERT INTO reviews (rating, review_date, author, review_text, restaurant) ' \
                f'VALUES ({rating}, "{review_date}", "{author}", "{review_text}", "{restaurant}")'
        with DatabaseActions.connection.cursor() as cursor:
            cursor.execute(query)
            DatabaseActions.connection.commit()
            cursor.close()
        DatabaseActions.connection.close()

    @staticmethod
    def convert_to_unvectorized_class(data):
        result = []
        for d in data:
            temp = Unvectorized(d[0], d[1])
            result.append(temp)
        return result
