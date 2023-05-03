from mysql.connector import connect

with connect(host="localhost", user="root", password="BackupDR") as connection:
    db_request = 'CREATE DATABASE reviews'
    with connection.cursor() as cursor:
        cursor.execute(db_request)
