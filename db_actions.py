from mysql.connector import connect
from get_config import get_data


class DatabaseActions:
    db_config = {
        "host": get_data('db_host'),
        "user": get_data('db_user'),
        "password": get_data('db_password'),
        "database": get_data('db_database'),
    }

    @staticmethod
    def get_all():
        with connect(**DatabaseActions.db_config) as con:
            query = 'SELECT * FROM reviews'
            with con.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        return result

    @staticmethod
    def add_element(rating, review_date, author, review_text, restaurant):
        with connect(**DatabaseActions.db_config) as con:
            query = f'INSERT INTO reviews (rating, review_date, author, review_text, restaurant) ' \
                    f'VALUES ({rating}, "{review_date}", "{author}", "{review_text}", "{restaurant}")'
            with con.cursor() as cursor:
                cursor.execute(query)
                con.commit()
    
    @staticmethod
    def get_parsed():
        with connect(**DatabaseActions.db_config) as con:
            query = 'SELECT review_text, vector, is_fake FROM reviews WHERE manually_tested = 1 and is_fake is not NULL'
            with con.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        return result

    @staticmethod
    def add_vector(id, vector):
        str_vector = vector.dumps().hex()

        with connect(**DatabaseActions.db_config) as con:
            query = f'UPDATE reviews ' \
                    f'SET vector = "{str_vector}" ' \
                    f'WHERE id = {id}'
                
            with con.cursor() as cursor:
                cursor.execute(query)
                con.commit()

# import numpy as np

# arr = np.array([0.23423, 2.3, 3, 4, 5, 6])
# ts = arr.tobytes()
# print(ts)
# print("-" * 70)
# arr2 = np.frombuffer(ts, dtype=float)


# for i in arr2: print(i)